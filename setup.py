from setuptools import setup

setup(
    name="tate-server",
    version="0.9",
    scripts=['run_tate_server','tate-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'tateserver':'src'
        },
    py_modules=[
        'tateserver.__init__',
        'tateserver.utils',
        'tateserver.storage',
        'tateserver.deserialize',
        'tateserver.networks',
        'tateserver.blockchain_processor',
        'tateserver.server_processor',
        'tateserver.processor',
        'tateserver.version',
        'tateserver.ircthread',
        'tateserver.stratum_tcp',
        'tateserver.stratum_http'
    ],
    description="Mazacoin Tate Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Tate lightweight Mazacoin wallet. Forked by mazaclub from Electrum-server."""
)


