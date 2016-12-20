#! /usr/bin/php

<?php

$path=$argv[1];

$data=json_decode(file_get_contents("$path/metadata.json"));

$dummy=explode('-',$data->{'name'});

$name=$dummy[1];

$version=explode('-',$data->{'version'});


?>

Summary:     <?php  echo $data->{'summary'} ?> 
Name:        puppet-module-<?php echo $data->{'name'} ?> 
Version:     <?php echo $version[0] ?> 
<?php if(count($version)==2){ ?>
Release:     <?php echo $version[1] ?> 
<?php }else { ?>
Release:     0
<?php } ?> 
# License is a compulsory field so you have to put something there.
License:      none
Source:       module.tar.gz
# This package doesn't contain any binary files so it's architecture independent, hence
# specify noarch for the BuildArch.
BuildArch:    noarch
BuildRoot:    %{_tmppath}/%{name}-build
<?php
foreach ($data->{'dependencies'} as $dep){
  $dep_name=str_replace('/','-',$dep->{"name"});
  if(preg_match('/^\S+$/',$dep->{"version_requirement"})){
    $dep->{"version_requirement"}='= '.$dep->{"version_requirement"};
  }elseif(preg_match('/^(\S+\s+){3}\S+$/',$dep->{"version_requirement"})){
    $dummy=explode(' ',$dep->{"version_requirement"});
    echo "Requires: puppet-module-".$dep_name." ".$dummy[0]." ".$dummy[1]."\n";
    $dep->{"version_requirement"}=$dummy[2]." ".$dummy[3];
  }
  echo "Requires: puppet-module-".$dep_name." ".$dep->{"version_requirement"}."\n";
}
?> 
# I don't worry too much about the group since now one uses the rpm except me
# There's a list at /usr/share/doc/packages/rpm/GROUPS but you don't have to use one of them
# I just use System/Base by default and only change it if something more suitable occurs to me
Group:          Puppet
Vendor:         sartiran@llr.in2p3.fr

%description
<?php echo  $data->{'description'} ?> 

%prep
# the set up macro unpacks the source bundle and changes in to the represented by
%setup -n etc/puppet/modules/<?php echo $name."\n"?> 

%build
# this section is empty for this example as we're not actually building anything

%install
# create directories where the files will be located
mkdir -p $RPM_BUILD_ROOT/etc/puppet/modules/<?php echo $name ?> 
cp -r * $RPM_BUILD_ROOT/etc/puppet/modules/<?php echo $name ?> 

%post
# the post section is where you can run commands after the rpm is installed.
#insserv /etc/init.d/my_maintenance

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

# list files owned by the package here
%files
%defattr(-,root,root)
/etc/puppet/modules/<?php echo $name ?> 

%changelog
