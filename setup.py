from distutils.core import setup
setup(
  name = 'rasa2sheets',         # How you named your package folder (MyLib)
  packages = ['rasa2sheets'],   # Chose the same as "name"
  version = '0.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Import and export Rasa components to csv/xls',   # Give a short description about your library
  author = 'Daniel Yudi',                   # Type in your xlsname
  author_email = 'danielyudicarvalho@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['RASA', 'SHEETS', 'CSV'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
          'pandas',
          'pyyaml'
      ],
  classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)