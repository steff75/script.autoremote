import xbmcaddon
import urllib2
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

devicekey = addon.getSetting('key')
message = urllib2.quote(addon.getSetting('message'))
timetolive = addon.getSetting('ttl')
password = urllib2.quote(addon.getSetting('password'))
group = urllib2.quote(addon.getSetting('group'))
target = urllib2.quote(addon.getSetting('target'))
sender = urllib2.quote(addon.getSetting('sender'))
req = 'https://autoremotejoaomgcd.appspot.com/sendmessage?key=' + devicekey + '&message=' + message + '&ttl=' + timetolive + '&password=' + password + '&collapseKey=' + group + '&target=' + target + '&sender=' + sender
 
xbmc.executebuiltin('Notification(%s, sending message ..., 1500)'%(addonname))
urllib2.urlopen(req)
