# Lab 11 – Discussion

**Karl Khouri**

## Part 1 – Installation packages

| Format | Used on | Tool | Description |
|--------|---------|------|-------------|
| MSI | Windows | WiX Toolset / Visual Studio, `msiexec` | Standard Windows installer: install, repair and remove software |
| DEB | Debian / Ubuntu | `dpkg-deb`, `dpkg`, `apt` | Contains the files and the metadata needed for installation |
| RPM | RedHat / Fedora / CentOS | `rpmbuild`, `rpm`, `yum` / `dnf` | RedHat's equivalent of DEB, with different tools and metadata (SPEC file) |

**Difference between DEB and RPM:** DEB packages are used on Debian-based distributions and are managed with `dpkg` and `apt`. RPM packages are used on RedHat-based distributions and are managed with `rpm` and `yum`/`dnf`. Both contain files and metadata, but they use different package systems and command-line tools.

## Part 2 – Components of an MSI package

An MSI file is a database made of tables (`Property`, `Directory`, `Component`, `File`, `Feature`, `Media`, ...) that `msiexec` reads to install, repair and uninstall the software. In `helloworld.wxs`:

- **Product / Package**: the metadata of the installer – name (`HelloWorld Karl Khouri`), version (`1.0.0`), manufacturer, language, `UpgradeCode` and install scope. This is what appears in Programs and Features.
- **Directories**: the folder tree on the target system. `TARGETDIR` → `ProgramFiles64Folder` → `HelloWorld`, so the files are installed in `C:\Program Files\HelloWorld\`.
- **Components**: the smallest unit that Windows Installer installs and tracks. Each component has a GUID and a key path. There is one component per file: `helloworld.exe`, `README.md` and `user_guide.txt`.
- **Features**: groups of components that the user installs together. `MainFeature` references the three components.
- **Media**: the files are compressed in a cabinet (`helloworld.cab`) that is embedded inside the `.msi`.

## Part 3 – Structure of a DEB package

A `.deb` file is an `ar` archive containing:

- `debian-binary` – the package format version (`2.0`)
- `control.tar` – the content of the `DEBIAN/` directory (the `control` file)
- `data.tar` – the files to install, with the same layout they will have under `/`

The build directory `myapp/` mirrors the target file system:

- `myapp/usr/local/bin/helloworld` – the application binary
- `myapp/usr/share/doc/myapp/` – the help file (`README.md`) and the user guide (`user_guide.txt`)
- `myapp/DEBIAN/control` – the package metadata

The **control file** defines the metadata used by `dpkg` and `apt` to install, upgrade, list and remove the package:

- `Package` – package name (`helloworld`, shown by `dpkg -l | grep helloworld`)
- `Version` – package version (`1.0`)
- `Section` and `Priority` – classification of the package
- `Architecture` – target architecture (`amd64`)
- `Maintainer` – name and email of the maintainer
- `Description` – short description of the application

The metadata can be checked with `dpkg-deb -I helloworld_karl_khouri.deb` and the contents with `dpkg-deb -c helloworld_karl_khouri.deb`.

## Part 4 – Role of the SPEC file

The SPEC file is the recipe that `rpmbuild` follows to create the RPM. It defines:

- **Name, Version, Release, Summary, License, Source0**: the package metadata and the source archive (`myapp-1.0.tar.gz`).
- **%description**: a description of the package.
- **%prep**: prepares the sources (`%setup -q` extracts the archive).
- **%install**: copies the files into the build root at their installation paths (`/usr/local/bin`, `/usr/share/doc/myapp`).
- **%files**: the list of files included in the package.
- **%changelog**: the history of changes to the package.

It controls the metadata, the build process, where the files are installed and which files are included in the RPM.

## Conclusion

Installation packages make software easy to install, maintain and remove, and keep the installation consistent across systems. In this lab the same Hello World application was packaged as an MSI with the WiX Toolset, as a DEB with `dpkg-deb`, and as an RPM with `rpmbuild`. The most challenging part is the metadata and the directory structure, because a small error in them breaks the build or the installation.
