"Given a bpn, add a special key to the parts that need to be translated"
def addSpecialKey(bpnFile, specialKey):
	"""
	Adds the specialKey to specific bpn parts and returns the updated bpn, containing the special key
	Parts that need to be updated are defined in this confluence page as TODO
		Say lemmas	REGEX name="say.*"
		Ask lemmas (NOT asking for a slot)	REGEX name="(ask |ask)&#34;.*&#34;"
		values on edges (EXPRESSION):	REGEX value="(.*(==|!=|bpn:choice).*)"
		Values variables are set to 	REGEX name="set the variable.*to.*"
		Strings in scripts that are used in buttons.	WILL DO manually unless I come up with a better regex/idea
	"""
	
	# TODO write pseudocode describing the steps to do that
	
	
	


def addKeyToAskLemmas(askRegex, specialKey):
	"""
	Returns the string after the addition of the special key. 
	"""

def addKeyToSayLemmas(sayRegex, specialKey):
	"""
	Returns the string after the addition of the special key. 
	"""

def addKeyToEdges(edgeRegex, specialKey):
	"""
	Returns the string after the addition of the special key. 
	"""

def addKeyToSetVariableTasks(setVarRegex, specialKey):
	"""
	Returns the string after the addition of the special key. 
	"""

