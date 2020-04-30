from setuptools import setup


# Include the README doc in pypi description
with open('README.md') as readme:
    long_description = readme.read()
long_description += '\n\n'
with open('CHANGES.txt') as changes:
    long_description += changes.read()


setup(
    name = 'sphinx-tabs',
    version = '2.0.0',
    author = 'scriptautomate',
    author_email = 'derek@icanteven.io',
    packages = ['sphinx_tabs', 'sphinx_tabs.test'],
    test_suite='sphinx_tabs.test',
    package_data = {
        'sphinx_tabs': [
            'tabs.js',
            'tabs.css',
            'semantic-ui-2.4.1/*',
        ],
    },
    data_files = [("", ["LICENSE"])],
    url = 'https://github.com/scriptautomate/sphinx-tabs',
    license = 'MIT',
    description = 'Tab views for Sphinx',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    install_requires = ['sphinx>=1.4'],
    tests_require = ['sphinx>=1.4', 'docutils', 'pygments', 'sphinx_testing', 'lxml'],
    python_requires = '>=3.5.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ]
)
