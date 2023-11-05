# Rightnow

Small routine to update a `now` static HTML page from console.

Uses a bash script, a python script (running into a virtual env), with BeautifulSoup and Markdown, a git repository.

## 1. Base requirements

[Tidy](http://www.html-tidy.org/) is required to beautify our HTML (that we want to look as nice as possible).

It might be already installed on your system. Check it out in your console by running:
```sh
tidy --version
```
If that fails, install it from a package manager:

-   MacOS, [Fink](http://www.finkproject.org/): `fink install tidy`
-   MacOS, [Homebrew](http://brew.sh/): `brew install tidy-html5`
-   MacOS, [MacPorts](https://www.macports.org/): `sudo port install tidy`
-   Windows, [Chocolatey](https://chocolatey.org/): `choco install html-tidy`
-   Linux, [Debian](http://www.debian.org/): `sudo apt install tidy`

## 2. Setup

Clone the repo, and remove its link to this one.

```sh
git clone https://github.com/jbidoret/rightnow.git /your/path/to/now
cd /your/path/to/now
git set-url origin git@github.com:your_own/repository.git
```
Create the virtualenv, install the dependencies. The main dependencies are [pytidylib](https://pythonhosted.org/pytidylib/) that allows tidyfication of the HTML, [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Markdown](https://python-markdown.github.io/), with [mdx-linkify](https://github.com/daGrevis/mdx_linkify) extension (to transform raw URLs into hyperlinks).

```sh
python -m venv env # create `env` virtualenv
source env/bin/activate # activate the venv
echo /env > .gitignore # ignore the venv
pip install -r requirements.txt # install dependencies
```


## 3. Configuration

Setup paths in `rightnow.py` and `rightnow.sh`.

In your `.bashrc` or `.zshrc`, alias the `now` command to `rightnow.sh`:
```sh
alias now='/your/path/to/now/rightnow.sh'
```

## 4. Run
```sh
now
```

Deploy strategy is out of the scope of this tool and doc. Github/Gitlab pages can be an option, a deploy script based on a hook can be another. 

Oldschoolars might prefer Rsync that the git-based workflow.