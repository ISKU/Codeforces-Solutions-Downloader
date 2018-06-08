Codeforces-Solutions-Downloader
==========
 `Codeforces-Solutions-Downloader` is a tool that solves various algorithmic problems in [Codeforces](http://codeforces.com/) and automatically downloads the accepted solution codes. This tool uses your handle to search and analyze the source code in Codeforces. If the source code does not exist in your local repository, save the source code file according to the directory name format and source name format options. **If you want to push the source code to [Github](https://github.com/), recommend [Codeforces-AutoCommit](https://github.com/ISKU/Codeforces-AutoCommit)**

Installation
----------
``` bash
$ git clone https://github.com/ISKU/Codeforces-Solutions-Downloader
```

**Dependency**
``` bash
$ pip3 install requests
$ pip3 install bs4
```

How to use
----------
- Run the tool as follows.
``` bash
$ python3 main.py
```
> - Search **all submitted** source code and analyze the correct source code.
> - If there are multiple correct source codes, select the **last submitted** source code.

- **Options:**

| **option**            | **Description**
|:-------------------|:-------------------------------------------------------------------------------------------
| **handle**         | Input your Codeforces handle (username)
| **mkdir**          | Decide if you want to create a directory when you save the source code. <br>(false: directory name option is ignored.)
| **directory name** | Set the name of the directory where the source code is saved.
| **source name**    | Set the name of the source code file.

> :bulb: [CONTEST]: If the content contains [CONTEST], it is replaced by contest_id. <br>
> :bulb: [INDEX]: If the content contains [INDEX], it is replaced by problem_index. <br>
> :bulb: [TITLE]: If the content contains [TITLE], it is replaced by problem_title.

License
----------
> - [MIT](LICENSE)

Author
----------
> - Minho Kim ([ISKU](https://github.com/ISKU))
> - http://codeforces.com/profile/isku
> - **E-mail:** minho.kim093@gmail.com
