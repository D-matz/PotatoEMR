from django.db import models
from .models_dir.FHIR_DataTypes.FHIR_primitive import *
from .models_dir.FHIR_DataTypes.FHIR_generalpurpose import *
from .models_dir.FHIR_DataTypes.FHIR_metadata import *

from .models_dir.FHIR_Resources.AllergyIntolerance import *
from .models_dir.FHIR_Resources.Appointment import *
from .models_dir.FHIR_Resources.Encounter import *
from .models_dir.FHIR_Resources.Immunization import *
from .models_dir.FHIR_Resources.Location import *
from .models_dir.FHIR_Resources.Observation import *
from .models_dir.FHIR_Resources.Patient import *
from .models_dir.FHIR_Resources.Practitioner import *
from .models_dir.FHIR_Resources.PractitionerRole import *
from .models_dir.FHIR_Resources.Slot import *

class FHIR_Account(models.Model): pass
class FHIR_ActivityDefinition(models.Model): pass
class FHIR_ActorDefinition(models.Model): pass
class FHIR_AdministrableProductDefinition(models.Model): pass
class FHIR_AdverseEvent(models.Model): pass
class FHIR_AppointmentResponse(models.Model): pass
class FHIR_ArtifactAssessment(models.Model): pass
class FHIR_AuditEvent(models.Model): pass
class FHIR_Basic(models.Model): pass
class FHIR_Binary(models.Model): pass
class FHIR_BiologicallyDerivedProduct(models.Model): pass
class FHIR_BiologicallyDerivedProductDispense(models.Model): pass
class FHIR_BodyStructure(models.Model): pass
class FHIR_Bundle(models.Model): pass
class FHIR_CapabilityStatement(models.Model): pass
class FHIR_CarePlan(models.Model): pass
class FHIR_CareTeam(models.Model): pass
class FHIR_ChargeItem(models.Model): pass
class FHIR_ChargeItemDefinition(models.Model): pass
class FHIR_Citation(models.Model): pass
class FHIR_Claim(models.Model): pass
class FHIR_ClaimResponse(models.Model): pass
class FHIR_ClinicalAssessment(models.Model): pass
class FHIR_ClinicalUseDefinition(models.Model): pass
class FHIR_CodeSystem(models.Model): pass
class FHIR_Communication(models.Model): pass
class FHIR_CommunicationRequest(models.Model): pass
class FHIR_CompartmentDefinition(models.Model): pass
class FHIR_Composition(models.Model): pass
class FHIR_ConceptMap(models.Model): pass
class FHIR_Condition(models.Model): pass
class FHIR_ConditionDefinition(models.Model): pass
class FHIR_Consent(models.Model): pass
class FHIR_Contract(models.Model): pass
class FHIR_Coverage(models.Model): pass
class FHIR_CoverageEligibilityRequest(models.Model): pass
class FHIR_CoverageEligibilityResponse(models.Model): pass
class FHIR_DetectedIssue(models.Model): pass
class FHIR_Device(models.Model): pass
class FHIR_DeviceAlert(models.Model): pass
class FHIR_DeviceAssociation(models.Model): pass
class FHIR_DeviceDefinition(models.Model): pass
class FHIR_DeviceDispense(models.Model): pass
class FHIR_DeviceMetric(models.Model): pass
class FHIR_DeviceRequest(models.Model): pass
class FHIR_DeviceUsage(models.Model): pass
class FHIR_DiagnosticReport(models.Model): pass
class FHIR_DocumentReference(models.Model): pass
class FHIR_EncounterHistory(models.Model): pass
class FHIR_Endpoint(models.Model): pass
class FHIR_EnrollmentRequest(models.Model): pass
class FHIR_EnrollmentResponse(models.Model): pass
class FHIR_EpisodeOfCare(models.Model): pass
class FHIR_EventDefinition(models.Model): pass
class FHIR_Evidence(models.Model): pass
class FHIR_EvidenceVariable(models.Model): pass
class FHIR_ExampleScenario(models.Model): pass
class FHIR_ExplanationOfBenefit(models.Model): pass
class FHIR_FamilyMemberHistory(models.Model): pass
class FHIR_Flag(models.Model): pass
class FHIR_FormularyItem(models.Model): pass
class FHIR_GenomicStudy(models.Model): pass
class FHIR_Goal(models.Model): pass
class FHIR_GraphDefinition(models.Model): pass
class FHIR_Group(models.Model): pass
class FHIR_GuidanceResponse(models.Model): pass
class FHIR_HealthcareService(models.Model): pass
class FHIR_ImagingSelection(models.Model): pass
class FHIR_ImagingStudy(models.Model): pass
class FHIR_ImmunizationEvaluation(models.Model): pass
class FHIR_ImmunizationRecommendation(models.Model): pass
class FHIR_ImplementationGuide(models.Model): pass
class FHIR_Ingredient(models.Model): pass
class FHIR_InsurancePlan(models.Model): pass
class FHIR_InsuranceProduct(models.Model): pass
class FHIR_InventoryItem(models.Model): pass
class FHIR_InventoryReport(models.Model): pass
class FHIR_Invoice(models.Model): pass
class FHIR_Library(models.Model): pass
class FHIR_Linkage(models.Model): pass
class FHIR_List(models.Model): pass
class FHIR_ManufacturedItemDefinition(models.Model): pass
class FHIR_Measure(models.Model): pass
class FHIR_MeasureReport(models.Model): pass
class FHIR_Medication(models.Model): pass
class FHIR_MedicationAdministration(models.Model): pass
class FHIR_MedicationDispense(models.Model): pass
class FHIR_MedicationKnowledge(models.Model): pass
class FHIR_MedicationRequest(models.Model): pass
class FHIR_MedicationStatement(models.Model): pass
class FHIR_MedicinalProductDefinition(models.Model): pass
class FHIR_MessageDefinition(models.Model): pass
class FHIR_MessageHeader(models.Model): pass
class FHIR_MolecularDefinition(models.Model): pass
class FHIR_MolecularSequence(models.Model): pass
class FHIR_NamingSystem(models.Model): pass
class FHIR_NutritionIntake(models.Model): pass
class FHIR_NutritionOrder(models.Model): pass
class FHIR_NutritionProduct(models.Model): pass
class FHIR_ObservationDefinition(models.Model): pass
class FHIR_OperationDefinition(models.Model): pass
class FHIR_OperationOutcome(models.Model): pass
class FHIR_Organization(models.Model): pass
class FHIR_OrganizationAffiliation(models.Model): pass
class FHIR_PackagedProductDefinition(models.Model): pass
class FHIR_Parameters(models.Model): pass
class FHIR_PaymentNotice(models.Model): pass
class FHIR_PaymentReconciliation(models.Model): pass
class FHIR_Permission(models.Model): pass
class FHIR_Person(models.Model): pass
class FHIR_PersonalRelationship(models.Model): pass
class FHIR_PlanDefinition(models.Model): pass
class FHIR_Procedure(models.Model): pass
class FHIR_Provenance(models.Model): pass
class FHIR_Questionnaire(models.Model): pass
class FHIR_QuestionnaireResponse(models.Model): pass
class FHIR_RegulatedAuthorization(models.Model): pass
class FHIR_RelatedPerson(models.Model): pass
class FHIR_Requirements(models.Model): pass
class FHIR_RequestOrchestration(models.Model): pass
class FHIR_ResearchStudy(models.Model): pass
class FHIR_ResearchSubject(models.Model): pass
class FHIR_RiskAssessment(models.Model): pass
class FHIR_Schedule(models.Model): pass
class FHIR_SearchParameter(models.Model): pass
class FHIR_ServiceRequest(models.Model): pass
class FHIR_SpecimenDefinition(models.Model): pass
class FHIR_Specimen(models.Model): pass
class FHIR_StructureDefinition(models.Model): pass
class FHIR_StructureMap(models.Model): pass
class FHIR_Subscription(models.Model): pass
class FHIR_SubscriptionStatus(models.Model): pass
class FHIR_SubscriptionTopic(models.Model): pass
class FHIR_Substance(models.Model): pass
class FHIR_SubstanceDefinition(models.Model): pass
class FHIR_SubstanceNucleicAcid(models.Model): pass
class FHIR_SubstancePolymer(models.Model): pass
class FHIR_SubstanceProtein(models.Model): pass
class FHIR_SubstanceReferenceInformation(models.Model): pass
class FHIR_SubstanceSourceMaterial(models.Model): pass
class FHIR_SupplyDelivery(models.Model): pass
class FHIR_SupplyRequest(models.Model): pass
class FHIR_Task(models.Model): pass
class FHIR_TerminologyCapabilities(models.Model): pass
class FHIR_TestPlan(models.Model): pass
class FHIR_TestReport(models.Model): pass
class FHIR_TestScript(models.Model): pass
class FHIR_Transport(models.Model): pass
class FHIR_ValueSet(models.Model): pass
class FHIR_VerificationResult(models.Model): pass
class FHIR_VisionPrescription(models.Model): pass
