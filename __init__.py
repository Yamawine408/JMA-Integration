from homeassistant.core import HomeAssistant

DOMAIN = "jma"

async def async_setup(hass, config):
    hass.states.async_set("jma.earthquake", None)
    return True

#async def async_setup_entry(
#    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
#) -> bool:
#    """Set up platform from a ConfigEntry."""
#    hass.data.setdefault(DOMAIN, {})
#    hass.data[DOMAIN][entry.entry_id] = entry.data
#
#    # Forward the setup to the sensor platform.
#    hass.async_create_task(
#        hass.config_entries.async_forward_entry_setup(entry, "sensor")
#    )
#    return True
