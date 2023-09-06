{
    "variables": {
        "openssl_fips": "",
    },
    "targets": [
        {
            "target_name": "fuse",
            "include_dirs": [
                "<!(node -e \"require('napi-macros')\")",
                "<!@(node -e \"require('fuse-shared-library/include')\")",
            ],
            "libraries": [
                "<!@(node -e \"require('fuse-shared-library/lib')\")",
            ],
            'xcode_settings': {
                'OTHER_CFLAGS': [
                    '-g',
                    '-O3',
                    '-Wall'
                ]
            },
            'cflags': [
                '-g',
                '-O3',
                '-Wall'
            ],
            "conditions": [
                ['OS!="win"', {"sources": ["fuse-native.c"]}],
                ['OS=="win"', {"sources": ["fuse-native.cpp"]}],
            ],
        },
        {
            "target_name": "postinstall",
            "type": "none",
            "dependencies": ["fuse"],
            "copies": [{
                "destination": "build/Release",
                "files": ["<!(node -e \"require('fuse-shared-library/lib')\")"],
            }],
            "conditions": [
                ['OS=="win"', {
                    "copies=": [
                        {"destination": "build/Release", "files": [
                            # expanding a variable to a list here does not seem to work somehow
                            "<!(node -e \"console.log(require('fuse-shared-library').bin)\")",
                            "<!(node -e \"console.log(require('fuse-shared-library').pthreads.bin)\")",
                        ]}
                    ],
                }]
            ],
        }
    ]
}
