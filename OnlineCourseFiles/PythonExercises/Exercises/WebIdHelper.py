import base64
import uuid

class WebIdHelper():

    def decodeType(encodedString):
        
        lookup = {
            "F": "Full",
            "I": "ID Only",
            "P": "Path Only",
            "L": "Local ID Only",
            "D": "Default ID Only"
        }
        return lookup[encodedString]
    
    def decodeVersion(encodedString):
        
        lookup = {
            "0": "WebId 1.0",
            "1": "WebId 2.0",
        }
        return lookup[encodedString]

    def decodeObjectMarker(encodedString):
        
        lookup = {
            "Xs": "AFAnalysis",
            "XC": "AFCategory",
            "XT": "AFAnalysisTemplate",
            "XR": "AFAnalysisRule",
            "XP": "AFPlugIn for Analysis Rule",
            "Ab": "AFAttribute",
            "AC": "AFCategory for Attribute",
            "AT": "AFAttributeTemplate",
            "RD": "AFDatabase",
            "Em": "AFElement",
            "EC": "AFCategory for Element",
            "ET": "AFElementTemplate",
            "MS": "AFEnumerationSet",
            "MV": "AFEnumerationValue",
            "Fm": "AFEventFrame",
            "Nf": "AFNotification",
            "NT": "AFNotificationTemplate",
            "TR": "AFTimeRule",
            "TP": "AFPlugIn for Time Rule",
            "SI": "AFSecurityIdentity",
            "SM": "AFSecurityMapping",
            "Bl": "AFTable",
            "BC": "AFCategory for Table",
            "DP": "PIPoint",
            "DS": "PIServer",
            "RS": "PISystem",
            "Ut": "UOM",
            "UC": "UOMClass"
        }
        return lookup[encodedString]

    def decodeGuid(encodedString):
        
        replacedString = encodedString.replace('-','+').replace('_','/')
        padNeeded = len(encodedString) % 4
        for i in range(padNeeded):
            replacedString = replacedString + '='
        
        b64bytes = replacedString.encode('utf-8')
        guid_bytes = base64.b64decode(b64bytes)
        guid = uuid.UUID(bytes_le=guid_bytes)
        return str(guid)

    def decodePath(encodedString):
        
        replacedString = encodedString.replace('-','+').replace('_','/')
        padNeeded = len(encodedString) % 4
        for i in range(padNeeded):
            replacedString = replacedString + '='
        
        b64bytes = replacedString.encode('utf-8')
        path_bytes = base64.b64decode(b64bytes)
        return str(path_bytes.decode('utf-8'))

   