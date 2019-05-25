from setuptools import setup

setup(
    name="giphybot",
    version="0.0.1",
    author="Wagner Macedo",
    url="http://gdgaracaju.com.br/",
    description="Giphy Bot",
    license="GPLv3",
    entry_points={
        'console_scripts': [
            'giphybot = giphybot.__main__:main',
        ],
    },
    packages=['giphybot'],
    install_requires=(
        'python-telegram-bot==11.1.0',
        'requests==2.22.0',
    ),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Topic :: Communications :: Chat",
    ],
)
