# Lab 11 – Configuration and Deployment Tools

**Karl Khouri**

A simple "Hello World" application packaged as an MSI (Windows), a DEB (Debian/Ubuntu) and an RPM (RedHat/Fedora).

Output of the application:

```
Hello, World from Karl_Khouri!
```

## Files

| File | Description |
|------|-------------|
| `helloworld.cpp` | C++ source for Windows (MSI) |
| `helloworld.c` | C source for Linux (DEB / RPM) |
| `helloworld.wxs` | WiX source used to build the MSI |
| `myapp/DEBIAN/control` | Debian control file (package metadata) |
| `myapp.spec` | RPM SPEC file |
| `README.md` | This file (help file) |
| `user_guide.txt` | User guide |
| `submission/` | Files to submit (`.msi`, `.deb`, `.rpm`, `source.zip`, `control`, screenshots) |

## Windows – C++ and MSI

Compile (MinGW):

```
g++ -static -o helloworld.exe helloworld.cpp
```

Run:

```
helloworld.exe
```

Build the MSI with the WiX Toolset (v3):

```
candle -arch x64 helloworld.wxs
light helloworld.wixobj -o helloworld_karl_khouri.msi
```

Or on Linux with `wixl` (msitools):

```
wixl -a x64 -o helloworld_karl_khouri.msi helloworld.wxs
```

Install and run:

```
msiexec /i helloworld_karl_khouri.msi /qb
"C:\Program Files\HelloWorld\helloworld.exe"
```

The application appears in **Control Panel > Programs and Features** as **HelloWorld Karl Khouri**.

Uninstall:

```
msiexec /x helloworld_karl_khouri.msi /qb
```

## Linux – C and DEB

Install the tools:

```
sudo apt-get install gcc dpkg-dev
```

Compile and run:

```
gcc -o helloworld helloworld.c
./helloworld
```

Create the package structure, copy the files and build the DEB:

```
mkdir -p myapp/DEBIAN
mkdir -p myapp/usr/local/bin
mkdir -p myapp/usr/share/doc/myapp
cp helloworld myapp/usr/local/bin/
cp README.md myapp/usr/share/doc/myapp/
cp user_guide.txt myapp/usr/share/doc/myapp/
dpkg-deb --build myapp helloworld_karl_khouri.deb
```

Inspect, install, run and verify:

```
dpkg-deb -c helloworld_karl_khouri.deb
dpkg-deb -I helloworld_karl_khouri.deb
sudo dpkg -i helloworld_karl_khouri.deb
helloworld
dpkg -l | grep helloworld
apt list --installed | grep helloworld
```

Uninstall:

```
sudo dpkg -r helloworld
```

## RedHat / Fedora – RPM (optional)

Install the tools:

```
sudo dnf install rpm-build
```

Create the directory structure, copy the files, create the source archive and build:

```
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
mkdir -p ~/rpmbuild/SOURCES/myapp-1.0
cp helloworld README.md user_guide.txt ~/rpmbuild/SOURCES/myapp-1.0/
tar -czf ~/rpmbuild/SOURCES/myapp-1.0.tar.gz -C ~/rpmbuild/SOURCES myapp-1.0
cp myapp.spec ~/rpmbuild/SPECS/
rpmbuild -ba ~/rpmbuild/SPECS/myapp.spec
```

The RPM is created in `~/rpmbuild/RPMS/x86_64/`.

Install, run and verify:

```
sudo rpm -i ~/rpmbuild/RPMS/x86_64/myapp-1.0-1*.x86_64.rpm
helloworld
rpm -qi myapp
```
