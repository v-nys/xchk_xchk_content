from xchk.contentviews import ContentView
from xchk.strats import *

class XchkConceptView(ContentView):

    uid = 'xchk_concept_1'
    template = 'checkerapp/what_is_xchk.html'
    mc_data = [("Is kennis lineair gestructureerd?",
                ("Ja",False,"Leert iedereen altijd alles in dezelfde volgorde?"),
                ("Nee",True,None)),
               ("Weten studenten altijd hoe ze studiemateriaal moeten benaderen?",
                ("Ja",False,"Waarom vragen we hen dan niet gewoon alles zelf op te zoeken?"),
                ("Nee",True,None)),
               ("Maken lectoren soms assumpties over voorkennis?",
                ("Ja",True,"Het is je nog nooit overkomen dat er iets gevraagd werd dat je niet in de les hebt gezien?"),
                ("Nee",False,None))] 
    custom_data = {'mc':mc_data}
    _accepting = ConjunctiveCheck([FileExistsCheck(extension='mc'),
                                   MultipleChoiceFormatCheck(),
                                   MultipleChoiceAnswerCheck(mc_data)])
    strat = Strategy(refusing_check=Negation(_accepting),
                     accepting_check=_accepting)
