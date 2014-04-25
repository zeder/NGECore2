import sys
from services.spawn import MobileTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	templates = Vector()
	templates.add('object/mobile/shared_bantha_hue.iff')
	mobileTemplate.setCreatureName('bantha')
	mobileTemplate.setTemplates(templates)
	mobileTemplate.setLevel(14)
	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	core.spawnService.addMobileTemplate('bantha', mobileTemplate)