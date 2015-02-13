Tate-server for the Tate client
=========================================
  
  * Original Author: Thomas Voegtlin (ThomasV on the bitcointalk forum)
  * Mazacoin Fork: Tyler Willis (kefkius)
  * Dockerfile/scripts: Rob Nelson (guruvan)
  * Language: Python

  * Integrated Docker image: [mazaclub/tateserver-mazacoind](https://registry.hub.docker.com/repos/mazaclub/tateserver-mazaclub)
  * Standalone Docker image [mazaclub/tate-server](https://registry.hub.docker.com/repos/mazaclub/tate-server)

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires bitcoind, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

  * The server knows which set of Bitcoin addresses belong to the same
    wallet, which might raise concerns about anonymity. However, it
    should be possible to write clients capable of using several
    servers.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. It is highly encouraged to use the provided Dockerfile and Docker or
     to use a more complete image: [mazaclub/tateserver-mazacoind](https://github.com/mazaclub/docker-tateserver-mazacoind)


License
-------

Electrum-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
