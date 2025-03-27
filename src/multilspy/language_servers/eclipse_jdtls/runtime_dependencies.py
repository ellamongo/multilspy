runtime_dependencies = {
    "_description": "This file lists the runtime dependencies for the Java Language Server",
    "gradle": {
        "platform-agnostic": {
            "url": "https://services.gradle.org/distributions/gradle-8.5-bin.zip",
            "archiveType": "zip",
            "relative_extraction_path": "."
        }
    },
    "vscode-java": {
        "darwin-arm64": {
            "url": "https://github.com/redhat-developer/vscode-java/releases/download/v1.23.0/java@darwin-arm64-1.23.0.vsix",
            "archiveType": "zip",
            "relative_extraction_path": "vscode-java"
        },
        "osx-arm64": {
            "url": "https://github.com/redhat-developer/vscode-java/releases/download/v1.39.0/java-darwin-arm64-1.39.0-439.vsix",
            "archiveType": "zip",
            "relative_extraction_path": "vscode-java",
            "jre_home_path": "extension/jre/21.0.5-macosx-aarch64",
            "jre_path": "extension/jre/21.0.5-macosx-aarch64/bin/java",
            "lombok_jar_path": "extension/lombok/lombok-1.18.34.jar",
            "jdtls_launcher_jar_path": "extension/server/plugins/org.eclipse.equinox.launcher_1.6.900.v20240613-2009.jar",
            "jdtls_readonly_config_path": "extension/server/config_mac_arm"
        },
        "linux-arm64": {
            "url": "https://github.com/redhat-developer/vscode-java/releases/download/v1.39.0/java-linux-arm64-1.39.0-439.vsix",
            "archiveType": "zip",
            "relative_extraction_path": "vscode-java",
            "jre_home_path": "extension/jre/21.0.5-linux-aarch64",
            "jre_path": "extension/jre/21.0.5-linux-aarch64/bin/java",
            "lombok_jar_path": "extension/lombok/lombok-1.18.34.jar",
            "jdtls_launcher_jar_path": "extension/server/plugins/org.eclipse.equinox.launcher_1.6.900.v20240613-2009.jar",
            "jdtls_readonly_config_path": "extension/server/config_linux_arm"
        },
        "linux-x64": {
            "url": "https://github.com/redhat-developer/vscode-java/releases/download/v1.39.0/java-linux-x64-1.39.0-439.vsix",
            "archiveType": "zip",
            "relative_extraction_path": "vscode-java",
            "jre_home_path": "extension/jre/21.0.5-linux-x86_64",
            "jre_path": "extension/jre/21.0.5-linux-x86_64/bin/java",
            "lombok_jar_path": "extension/lombok/lombok-1.18.34.jar",
            "jdtls_launcher_jar_path": "extension/server/plugins/org.eclipse.equinox.launcher_1.6.900.v20240613-2009.jar",
            "jdtls_readonly_config_path": "extension/server/config_linux"
        },
        "win-x64": {
            "url": "https://github.com/redhat-developer/vscode-java/releases/download/v1.39.0/java-win32-x64-1.39.0-439.vsix",
            "archiveType": "zip",
            "relative_extraction_path": "vscode-java",
            "jre_home_path": "extension/jre/21.0.5-win32-x86_64",
            "jre_path": "extension/jre/21.0.5-win32-x86_64/bin/java.exe",
            "lombok_jar_path": "extension/lombok/lombok-1.18.34.jar",
            "jdtls_launcher_jar_path": "extension/server/plugins/org.eclipse.equinox.launcher_1.6.900.v20240613-2009.jar",
            "jdtls_readonly_config_path": "extension/server/config_win"
        }
    },
    "intellicode": {
        "platform-agnostic": {
            "url": "https://VisualStudioExptTeam.gallery.vsassets.io/_apis/public/gallery/publisher/VisualStudioExptTeam/extension/vscodeintellicode/1.2.30/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage",
            "alternate_url": "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/VisualStudioExptTeam/vsextensions/vscodeintellicode/1.2.30/vspackage",
            "archiveType": "zip",
            "relative_extraction_path": "intellicode",
            "intellicode_jar_path": "extension/dist/com.microsoft.jdtls.intellicode.core-0.7.0.jar",
            "intellisense_members_path": "extension/dist/bundledModels/java_intellisense-members"
        }
    }
}