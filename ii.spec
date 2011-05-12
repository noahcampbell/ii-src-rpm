Name:           ii
Version:       	1.6 
Release:        1%{?dist}
Summary:       	Filesystem Based IRC Client 

Group:          Software
License:       	MIT 
URL:            http://tools.suckless.org/ii/ 
Source0:        http://dl.suckless.org/tools/ii-1.6.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  
#Requires:       

%description
ii is a minimalist FIFO and filesystem-based IRC client. It creates an irc directory tree with server, channel and nick name directories. In every directory a FIFO in file and a normal out file is created.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/bin/ii
%doc /usr/local/share/doc/ii/CHANGES
%doc /usr/local/share/doc/ii/FAQ
%doc /usr/local/share/doc/ii/LICENSE
%doc /usr/local/share/doc/ii/README
%doc /usr/local/share/doc/ii/query.sh
%doc /usr/local/share/man/man1/ii.1


%changelog
