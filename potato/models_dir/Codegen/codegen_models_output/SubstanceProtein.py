#FHIR Resource created by python potato/models_dir/Codegen/codegen_models.py
from django.db import models
from ..FHIR_DataTypes.FHIR_generalpurpose import *
from ..FHIR_DataTypes.FHIR_specialpurpose import *
from ..FHIR_DataTypes.FHIR_metadata import *
from ..FHIR_DataTypes.FHIR_primitive import *

class FHIR_SubstanceProtein(models.Model):
    BINDING_sequenceType = "TODO"
    sequenceType_cc = models.ManyToManyField(FHIR_GP_Coding, limit_choices_to={"codings__binding_rule": BINDING_sequenceType}, related_name='SubstanceProtein_sequenceType', blank=True)
    sequenceType_cctext = FHIR_primitive_StringField(max_length=5000, null=True, blank=True)

class FHIR_SubstanceProtein_disulfideLinkage(models.Model):
    SubstanceProtein = models.ForeignKey(FHIR_SubstanceProtein, related_name='SubstanceProtein_disulfideLinkage', null=False, on_delete=models.CASCADE)
    
    disulfideLinkage = FHIR_primitive_StringField(null=True, blank=True, )
    
class FHIR_SubstanceProtein_subunit(models.Model):
    SubstanceProtein = models.ForeignKey(FHIR_SubstanceProtein, related_name='SubstanceProtein_subunit', null=False, on_delete=models.CASCADE)
    sequence = FHIR_primitive_StringField(null=True, blank=True, )
    sequenceAttachment = models.OneToOneField("FHIR_GP_Attachment", related_name='SubstanceProtein_subunit_sequenceAttachment', null=True, blank=True, on_delete=models.SET_NULL)
    nTerminalModificationId = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceProtein_subunit_nTerminalModificationId', null=True, blank=True, on_delete=models.SET_NULL)
    nTerminalModification = FHIR_primitive_StringField(null=True, blank=True, )
    cTerminalModificationId = models.OneToOneField("FHIR_GP_Identifier", related_name='SubstanceProtein_subunit_cTerminalModificationId', null=True, blank=True, on_delete=models.SET_NULL)
    cTerminalModification = FHIR_primitive_StringField(null=True, blank=True, )
