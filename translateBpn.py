mockupJson = {
	"bpns": {
		"name" :  "BPN1",
		"languages" : {
			"EN": {
				"toTranslate": "translation",
				"more translations": "more"
			},
			"SE": {
				"and more": "more"
			}
		}
	}
}

def translateBpn(bpnInput, translations):
	"""
	returns the translated bpn (xml)
	"""

	#Identify all keys to be replaced in the bpn based on the agreed regex 
	# TODO come up with sth better than $$...$$: use different chars at beggining and end 


def parseTranslations(translations):
	"""
	returns a language specific(EN, SE, etc) translation dictionary in the format "key":"value", where key is the sentence to translate and value is the translated sentence of that key.
	"""

def replaceKeysInBpn(bpnInput, t):
	"""

	"""
# Things to think of: JSON format
"""
{ 
	"languages" : {
		"EN": {
			"bpns": {
				"name" :  "BPN1",
				"translations": {
					"toTranslate": "translation",
					"more translations": "more"
				}
			}
		}
	}
}

As per Hugo's suggestion
{
	"bpns": {
		"name" :  "BPN1",
		"languages" : {
			"EN": {
				"toTranslate": "translation",
				"more translations": "more"
			},
			"SE": {
				"and more": "more"
			}
		}
	}
}
"""

"""Export a BPN from dev
Put keys in the parts that need to be translated 
Create the mockup JSON for EN
Write the script
Run your script and check"""