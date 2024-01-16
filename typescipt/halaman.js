// Load the XML and XSLT files
const xmlFile = require("./xml.xml");
const xsltFile = require("./xslt.xsl");

// Create an XSLT processor
const processor = new XSLTProcessor();

// Load the XSLT into the processor
processor.importStylesheet(xsltFile);

// Transform the XML using the XSLT
const transformedXML = processor.transformToDocument(xmlFile);

// Create a new div element
const divElement = document.createElement("div");

// Add the transformed XML to the div element
divElement.innerHTML = transformedXML.documentElement.textContent;

// Append the div element to the document
document.body.appendChild(divElement);
