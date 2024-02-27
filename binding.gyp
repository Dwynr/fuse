{
    "variables": {
        "openssl_fips": "",
    },

    "targets": [
        {
            "target_name": "fuse",
            "include_dirs": ["<!(node -e \"require('napi-macros')\")"],
            'cflags': ['-g', '-O3', '-Wall'],

            "conditions": [
                ["OS=='linux' and target_arch=='x64'", {
                    "include_dirs+": ["<(module_root_dir)/lib/linux-x64/include"],
                    "libraries+": ["<(module_root_dir)/lib/linux-x64/lib/libfuse.so"],
                    "sources=": ["fuse.c"]
                }],

                ["OS=='linux' and target_arch=='arm'", {
                    "include_dirs+": ["<(module_root_dir)/lib/linux-arm/include"],
                    "libraries+": ["<(module_root_dir)/lib/linux-arm/lib/libfuse.so"],
                    "sources=": ["fuse.c"]
                }],

                ["OS=='mac' and target_arch=='x64'", {
                    "include_dirs+": ["<(module_root_dir)/lib/mac-x64/include"],
                    "libraries+": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"],
                    "sources=": ["fuse.c"],
                    'xcode_settings': {'OTHER_CFLAGS': ['-g', '-O3', '-Wall']},
                }],

                ["OS=='mac' and target_arch=='arm'", {
                    "include_dirs+": ["<(module_root_dir)/lib/mac-x64/include"],
                    "libraries+": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"],
                    "sources=": ["fuse.c"],
                    'xcode_settings': {'OTHER_CFLAGS': ['-g', '-O3', '-Wall']},
                }],

                ["OS=='mac' and target_arch=='arm64'", {
                    "include_dirs+": ["<(module_root_dir)/lib/mac-x64/include"],
                    "libraries+": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"],
                    "sources=": ["fuse.c"],
                    'xcode_settings': {'OTHER_CFLAGS': ['-g', '-O3', '-Wall']},
                }],

                ["OS=='win' and target_arch=='x64'", {
                    "include_dirs+": [
                        "<!(echo %ProgramFiles(x86)%)/WinFsp/inc/fuse",
                        "<(module_root_dir)/lib/win-x64/include",
                    ],
                    "libraries+": [
                        "<!(echo %ProgramFiles(x86)%)/WinFsp/lib/winfsp-x64.lib",
                        "<(module_root_dir)/lib/win-x64/lib/pthreadVC3.lib",
                    ],
                    "sources=": ["fuse.cpp"]
                }],
            ],
        },

        {
            "target_name": "postinstall",
            "type": "none",
            "dependencies": ["fuse"],

            "conditions": [
                ["OS=='linux' and target_arch=='x64'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": ["<(module_root_dir)/lib/linux-x64/lib/libfuse.so"]
                    }],
                }],

                ["OS=='linux' and target_arch=='arm'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": ["<(module_root_dir)/lib/linux-arm/lib/libfuse.so"]
                    }],
                }],

                ["OS=='mac' and target_arch=='x64'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"]
                    }],
                }],

                ["OS=='mac' and target_arch=='arm'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"]
                    }],
                }],

                ["OS=='mac' and target_arch=='arm64'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": ["<(module_root_dir)/lib/mac-x64/libosxfuse.2.dylib"]
                    }],
                }],

                ["OS=='win' and target_arch=='x64'", {
                    "copies=": [{
                        "destination": "build/Release",
                        "files": [
                                "<!(echo %ProgramFiles(x86)%)/WinFsp/bin/winfsp-x64.dll",
                                "<(module_root_dir)/lib/win-x64/bin/pthreadVC3.dll",
                                ]
                    }],
                }]
            ],
        }
    ]
}
