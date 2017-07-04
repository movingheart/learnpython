try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'ex47',
  'author': 'alan wan',
  'url': 'www.wanhuqianjia.com',
  'download_url': 'www.wanhuqianjia.com/download',
  'author_email': 'wst.521@163.com',
  'version': '0.1', 
  'install_requires': ['nose'],
  'packages': ['ex48'],
  'scripts': [],
  'name': 'skeleton'
}
setup(**config)
