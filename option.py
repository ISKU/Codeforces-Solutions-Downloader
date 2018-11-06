class Option:

    def __init__(self, user_info):
        self.user_info = user_info
        self.handle = user_info['handle']

    def source_tree(self, solved):
        if self.mkdir():
            return '%s/%s/' % (self.handle, self.dir_name(solved))
        return '%s/' % (self.handle)

    def mkdir(self):
        return self.user_info['mkdir']

    def dir_name(self, solved):
        return self.replace_info(self.user_info['dir_name'], solved)

    def source_name(self, solved):
        return self.replace_info(self.user_info['source_name'], solved)

    def replace_info(self, value, solved):
        value = value.replace('[CONTEST]', str(solved['contest_id']))
        value = value.replace('[INDEX]', solved['problem_id'])
        value = value.replace('[TITLE]', solved['problem_title'])
        value = self.replace_char(value)
        return value

    def replace_char(self, value):
        if self.user_info['os'] == 'Windows':
            value = value.replace(':', '：')
            value = value.replace('?', '？')
        value = value.replace('/', '／')
        value = value.replace('*', '＊')
        value = value.replace('"', '＂')
        value = value.replace('<', '＜')
        value = value.replace('>', '＞')
        value = value.replace('\\', '＼')
        value = value.replace('|', '｜')
        return value

    def get_ext(self, language):
        return {
            'GNU C': '.c',
            'GNU C11': '.c',
            'Clang++17 Diagnostics': '.cpp',
            'GNU C++': '.cpp',
            'GNU C++11': '.cpp',
            'GNU C++14': '.cpp',
            'GNU C++17': '.cpp',
            'GNU C++17 Diagnostics': '.cpp',
            'MS C++': '.cpp',
            'Mono C#': '.cs',
            'D': '.d',
            'Go': '.go',
            'Haskell': '.hs',
            'Java 8': '.java',
            'Kotlin': '.kt',
            'Ocaml': '.ml',
            'Delphi': '.dpr',
            'FPC': '.pas',
            'PascalABC.NET': '.pas',
            'Perl': '.pl',
            'PHP': '.php',
            'Python 2': '.py',
            'Python 3': '.py',
            'PyPy 2': '.py',
            'PyPy 3': '.py',
            'Ruby': '.rb',
            'Rust': '.rs',
            'Scala': '.scala',
            'JavaScript': '.js',
            'Node.js': '.js',
            'Q#': '.qs'
        }[language]
