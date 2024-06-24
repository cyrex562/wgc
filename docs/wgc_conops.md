# WGC CONOPs

* wgc
  * -v, --verbose: sets the verbosity level of the output
  * -c, --config <PATH_TO_WG_CONF>: required for all commands except `gen private-key` and `gen preshared-key`
  * -s, --setings <PATH_TO_SETTINGS>: settings file to use; if not specified, assumes default settings instead.
  * -j, --json: output in JSON format
  * show
    * requires `-c` to be specified, if not specified of invalid, then exit with an error
    * `config`: dump the configuration file
    * `peers`: dump a list of peers, including address, public key, endpoint, and allowed IPs
    * `addresses`: dump a list of all addresses for the configuration's network, used, and unused
    * `used-addresses`: dump a list of all used addresses
    * `unused-addresses`: dump a list of unused addresses
    * `public-key -k <PRIVATE_KEY>` : dump the public key for the specified private key
      * -k, --private-key: the private key to get a public key for
  * gen
    * `private-key`: generate a new private key
    * `preshared-key`: generate a new preshared key
  * config
    * `add-client-peer -a <ALLOWED_IP>`: add a new client peer to the configuration, dump the new configuration to the screen, and optionally save to disk
    * `add-server-peer -e <ENDPOINT_IP_PORT> -k <PUBLIC_KEY> -a <ALLOWED_IP>`: add a new server peer to the configuration
    * `remove-peer -k <PUBLIC_KEY>`: remove a peer from the configuration
    * `edit`: edit the config file with the system default editor