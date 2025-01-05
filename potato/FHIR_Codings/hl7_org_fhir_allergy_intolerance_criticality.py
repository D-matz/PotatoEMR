system = "http://hl7.org/fhir/allergy-intolerance-criticality"
version = "5.0.0"
coding = [
        {
            "code": "low",
            "display": "Low Risk",
            "definition": "Worst case result of a future exposure is not assessed to be life-threatening or having high potential for organ system failure."
        },
        {
            "code": "high",
            "display": "High Risk",
            "definition": "Worst case result of a future exposure is assessed to be life-threatening or having high potential for organ system failure."    
        },
        {
            "code": "unable-to-assess",
            "display": "Unable to Assess Risk",
            "definition": "Unable to assess the worst case result of a future exposure."
        }
]
