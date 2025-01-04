from django.db import models
from .FHIR_DataTypes.FHIR_primitive import *
from .FHIR_DataTypes.FHIR_generalpurpose import *
#keeping resources in separate files repeats some import boilerplate
#but maybe easier to manage when there are a lot of resources (nicer git history?)
from .FHIR_Resources.Event import *
from .FHIR_Resources.Device import *
from .FHIR_Resources.Organization import *
from .FHIR_Resources.Patient import *
from .FHIR_Resources.Practitioner import *
from .FHIR_Resources.PractitionerRole import *
from .FHIR_Resources.RelatedPerson import *
from .FHIR_Resources.Encounter import *
from .FHIR_Resources.CareTeam import *
from .FHIR_Resources.Observation import *
from .FHIR_Resources.AllergyIntolerance import *
    
