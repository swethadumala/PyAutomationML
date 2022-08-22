structure_dict = {
    'AdditionalData': {
        'abbreviation': 'AddData',
        'attributes': [],
        'children': ['AutomationMLVersion', 'WriterHeader'],
        'multi': True,
        'tags': []
    },
    'AdditionalInformation': {
        'abbreviation': 'AddInf',
        'attributes': ['WriterHeader'],
        'children': ['AutomationMLVersion', 'WriterHeader'],
        'multi': True,
        'tags': ['AutomationMLVersion',
            'UserDefined',
            'AMLV'
        ]
    },
    'Attribute': {
        'abbreviation': 'Attr',
        'attributes': ['Value',
            'Description',
            'DefaultValue',
            'RefSemantic'
        ],
        'children': ['Attribute'],
        'multi': True,
        'tags': ['ID', 'Name', 'AttributeDataType', 'Unit'],
        'sorted': ['ID', 'Name', 'ChangeMode', 'Unit', 'AttributeDataType', 'Value', 'Description', 'DefaultValue', 'RefSemantic', 'AMLHeader']
    },
    'AttributeNameMapping': {
        'abbreviation': 'AttrNameMapp',
        'attributes': [],
        'children': [],
        'multi': True,
        'tags': []
    },
    'AutomationMLVersion': {
        'abbreviation': 'AMLV',
        'attributes': [],
        'children': [],
        'multi': False,
        'tags': []
    },
    'CAEXFile': {
        'abbreviation': 'CAEXFile',
        'attributes': ['AdditionalInformation'],
        'children': ['AdditionalInformation',
            'AdditionalData',
            'RoleClassLib',
            'InterfaceClassLib',
            'SystemUnitClassLib',
            'InstanceHierarchy'
        ],
        'multi': False,
        'tags': ['FileName', 'SchemaVersion']
    },
    'ExternalInterface': {
        'abbreviation': 'EI',
        'attributes': [],
        'children': ['InternalElement', 'Attribute'],
        'multi': True,
        'tags': ['ID', 'Name', 'RefBaseClassPath'],
        'sorted': ['ID', 'Name', 'ChangeMode', 'RefBaseClassPath', 'AMLHeader']
    },
    'InstanceHierarchy': {
        'abbreviation': 'IH',
        'attributes': [],
        'children': ['Version', 'InternalElement'],
        'multi': True,
        'tags': ['ID', 'Name']
    },
    'InterfaceClass': {
        'abbreviation': 'IC',
        'attributes': ['Description'],
        'children': ['Attribute', 'InterfaceClass'],
        'multi': True,
        'tags': ['Name', 'RefBaseClassPath', 'ID']
    },
    'InterfaceClassLib': {
        'abbreviation': 'ICL',
        'attributes': ['Description', 'Version'],
        'children': ['InterfaceClass'],
        'multi': True,
        'tags': ['Name', 'ChangeMode', 'ID']
    },
    'InterfaceNameMapping': {
        'abbreviation': 'INM',
        'attributes': [],
        'children': [],
        'multi': True,
        'tags': []
    },
    'InternalElement': {
        'abbreviation': 'IE',
        'attributes': ['SupportedRoleClass'],
        'children': ['MappingObject',
            'RoleRequirement',
            'InternalElement',
            'Attribute',
            'ExternalInterface',
            'SupportedRoleClass',
            'InternalLink'
        ],
        'multi': True,
        'tags': ['ID', 'Name'],
        'sorted': ['ID', 'Name', 'SupportedRoleClass', 'ChangeMode', 'RefBaseSystemUnitPath', 'AMLHeader']
    },
    'InternalLink': {
        'abbreviation': 'IL',
        'attributes': [],
        'children': [],
        'multi': True,
        'tags': ['Name', 'ID', 'RefPartnerSideA', 'RefParterSideB']
    },
    'MappingObject': {
        'abbreviation': 'MO',
        'attributes': [],
        'children': ['AttributeNameMapping', 'InterfaceNameMapping'],
        'multi': False,
        'tags': []
    },
    'RefSemantic': {
        'abbreviation': 'RS',
        'attributes': [],
        'children': [],
        'multi': True,
        'tags': ['CorrespondingAttributePath']
    },
    'RoleClass': {
        'abbreviation': 'RC',
        'attributes': ['Revision'],
        'children': ['Attribute', 'ExternalInterface', 'RoleClass'],
        'multi': True,
        'tags': ['Name', 'RefBaseClassPath', 'ChangeMode', 'ID']
    },
    'RoleClassLib': {
        'abbreviation': 'RCL',
        'attributes': ['Description', 'Version'],
        'children': ['RoleClass'],
        'multi': True,
        'tags': ['Name', 'ChangeMode', 'ID']
    },
    'RoleRequirement': {
        'abbreviation': 'RR',
        'attributes': [],
        'children': [],
        'multi': True,
        'tags': []
    },
    'SupportedRoleClass': {
        'abbreviation': 'SRC',
        'attributes': [],
        'children': ['MappingObject'],
        'multi': True,
        'tags': ['RefRoleClassPath']
    },
    'SystemUnitClass': {
        'abbreviation': 'SUC',
        'attributes': ['SupportedRoleClass'],
        'children': ['InternalElement',
            'Attribute',
            'ExternalInterface',
            'SupportedRoleClass',
            'InternalLink',
            'SystemUnitClass'
        ],
        'multi': True,
        'tags': ['ID', 'Name', 'RefBaseClassPath', 'ChangeMode']
    },
    'SystemUnitClassLib': {
        'abbreviation': 'SUCL',
        'attributes': [],
        'children': ['SystemUnitClass'],
        'multi': True,
        'tags': ['ID', 'Name']
    },
    'WriterHeader': {
        'abbreviation': 'WH',
        'attributes': ['WriterName',
            'WriterID',
            'WriterVendor',
            'WriterVendorURL',
            'WriterVersion',
            'WriterRelease',
            'LastWritingDateTime',
            'WriterProjectTitle',
            'WriterProjectID'
        ],
        'children': [],
        'multi': False,
        'tags': []
    }
}