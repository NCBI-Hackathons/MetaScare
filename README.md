# MetaScare
A Pipeline to Compare Concepts in Funded Grants, BioProjects, and BioSamples

# What is the problem?
Research projects often change over time, but funding institutions would like to know how the project progression and data being collected differ from the awarded grant application to ensure that research remains in the scope of the original proposal. Currently, there's no user-friendly way to verify this outside of progress reports and publications. 

# How can we solve it?
In 2015, BioProject started making the Grant information a required field, providing a way for the BioProject and BioSamples collected within it to be linked to the grant application. When combined with data from RePORTER, the NIH research portfolio online reporting tool, we can use text mining to determine the degree of overlap between the grant application and the submitted BioProject and collected BioSamples, ensuring that the research stays in scope and easily indicating potential changes in the project progression.

# Workflow
BioProject → advanced search → Funding Agency = “NIH” → send to file: xml

