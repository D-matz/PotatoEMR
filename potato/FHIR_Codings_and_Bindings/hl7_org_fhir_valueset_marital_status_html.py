binding = "https://www.hl7.org/fhir/valueset-marital-status.html"
codings = [
{
"system" : "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus",
"version" : "???",
"coding" : [{'code': 'A', 'display': 'Annulled', 'definition': 'Marriage contract has been declared null and to not have existed'}, {'code': 'D', 'display': 'Divorced', 'definition': 'Marriage contract has been declared dissolved and inactive'}, {'code': 'I', 'display': 'Interlocutory', 'definition': 'Subject to an Interlocutory Decree.'}, {'code': 'L', 'display': 'Legally Separated', 'definition': ''}, {'code': 'M', 'display': 'Married', 'definition': 'A current marriage contract is active'}, {'code': 'C', 'display': 'Common Law', 'definition': "a marriage recognized in some jurisdictions and based on the parties' agreement to consider themselves married and can also be based on documentation of cohabitation.This definition was based on https://www.merriam-webster.com/dictionary/common-law%20marriage."}, {'code': 'P', 'display': 'Polygamous', 'definition': 'More than 1 current spouse'}, {'code': 'T', 'display': 'Domestic partner', 'definition': 'Person declares that a domestic partner relationship exists.'}, {'code': 'U', 'display': 'unmarried', 'definition': 'Currently not in a marriage contract.'}, {'code': 'S', 'display': 'Never Married', 'definition': 'No marriage contract has ever been entered'}, {'code': 'W', 'display': 'Widowed', 'definition': 'The spouse has died'}]
},
{
"system" : "http://terminology.hl7.org/CodeSystem/v3-NullFlavor",
"version" : "???",
"coding" : [{'code': 'UNK', 'display': 'unknown', 'definition': '**Description:**A proper value is applicable, but not known.Usage Notes: This means the actual value is not known. If the only thing that is unknown is how to properly express the value in the necessary constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used. No properties should be included for a datatype with this property unless:Those properties themselves directly translate to a semantic of "unknown". (E.g. a local code sent as a translation that conveys \'unknown\')Those properties further qualify the nature of what is unknown. (E.g. specifying a use code of "H" and a URL prefix of "tel:" to convey that it is the home phone number that is unknown.)'}]
},
]
