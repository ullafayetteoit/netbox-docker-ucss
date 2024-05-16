# Add your plugins and plugin settings here.
# Of course uncomment this file out.

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

# PLUGINS = ["netbox_bgp"]

# PLUGINS_CONFIG = {
#   "netbox_bgp": {
#     ADD YOUR SETTINGS HERE
#   }
# }

# # Enable installed plugins. Add the name of each plugin to the list.
PLUGINS = ['netbox_dns']

# # Plugins configuration settings. These settings are used by various plugins that the user may have installed.
# # Each key in the dictionary is the name of an installed plugin and its value is a dictionary of settings.
PLUGINS_CONFIG = {
  'netbox_dns': {
    'tolerate_non_rfc1035_types': ["TXT"],
    'tolerate_underscores_in_hostnames': True,
    'feature_ipam_coupling': True,
  },
}
