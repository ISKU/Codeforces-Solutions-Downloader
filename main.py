import sys
import os
import platform
from crawler import Crawler
from option import Option

class Main:

    def __init__(self, crawler, option, user_info):
        self.crawler = crawler
        self.option = option
        self.user_info = user_info

        self.handle = user_info['handle']
        self.solved_list = []

    def run(self):
        self.init()
        self.find_solved_problem()
        self.download_solutions()

    def init(self):
        if os.path.isdir(self.handle):
            sys.exit("\n* ERROR: Directory '%s' already exists." % (self.handle))
        os.makedirs(self.handle)

    def find_solved_problem(self):
        print('\n* find solved problem... ')
        self.solved_list = []
        solved_set = set()

        user_status_error, user_status = self.crawler.get_user_status(self.handle)
        if user_status_error:
            sys.exit('\n* ERROR: get_user_status, %s' % (user_status))

        for submission in user_status:
            if not submission['verdict'] == 'OK' or len(submission['problem']['tags']) == 0:
                continue

            key = str(submission['contestId']) + submission['problem']['index']
            if key in solved_set:
                continue
            solved_set.add(key)

            solved = {}
            solved['submission_id'] = submission['id']
            solved['contest_id'] = submission['contestId']
            solved['problem_id'] = submission['problem']['index']
            solved['problem_title'] = submission['problem']['name']
            solved['language'] = submission['programmingLanguage']
            self.solved_list.append(solved)

    def download_solutions(self):
        success = 0
        fail = 0

        for solved in self.solved_list:
            submission_id = solved['submission_id']
            contest_id = solved['contest_id']
            problem_id = solved['problem_id']
            language = solved['language']

            source_tree = self.option.source_tree(solved)
            source_name = self.option.source_name(solved)
            ext_error, source_ext = self.option.get_ext(language)
            if ext_error:
                print('\n* ERROR: get_ext, ' + source_ext)
                print('* Failed to download the source (submission: %d, contest: %d, index: %s)\n' % (submission_id, contest_id, problem_id))
                fail += 1
                continue

            file_path = '%s%s%s' % (source_tree, source_name, source_ext)
            if os.path.exists(file_path):
                print('* source already exists (submission: %d, contest: %d, index: %s)' % (submission_id, contest_id, problem_id))
                fail += 1
                continue
       
            source_error, source = self.crawler.get_source(submission_id, contest_id)
            if source_error:
                print('\n* ERROR: get_source, ' + source)
                print('* Failed to download the source (submission: %d, contest: %d, index: %s)\n' % (submission_id, contest_id, problem_id))
                fail += 1
                continue

            self.save_source(source_tree, file_path, source)
            print("* Successfully saved the '%s'" % (file_path))
            success += 1

        print('\n* Total: %d, Success: %d, Fail: %d' % (success + fail, success, fail))

    def save_source(self, source_tree, file_path, source):
        if not os.path.isdir(source_tree):
            os.makedirs(source_tree)

        f = open(file_path, 'w')
        f.write(source)
        f.close()

if __name__ == '__main__':
    try:
        user_info = {}
        
        if platform.system() == 'Windows':
            user_info['os'] = 'Windows'
        elif platform.system() == 'Linux':
            user_info['os'] = 'Linux'
        elif platform.system() == 'Darwin':
            user_info['os'] = 'Darwin'

        user_info['handle'] = input('* Codeforces Handle: ')

        mkdir = input('* mkdir option [true/false]: ')
        while True:
            if mkdir == 'true' or mkdir == 'false':
                break
            mkdir = input('* mkdir option [true/false]: ')
    
        if mkdir == 'false':
            user_info['mkdir'] = False
        if mkdir == 'true':
            user_info['mkdir'] = True
            user_info['dir_name'] = input('* directory name format: ')

        user_info['source_name'] = input('* source name format: ')

        crawler = Crawler()
        option = Option(user_info)
        Main(crawler, option, user_info).run()
    except KeyboardInterrupt:
        print('\n* bye\n')
