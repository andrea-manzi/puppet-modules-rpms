# puppet-modules-rpms

Few scripts for creating rpm's from puppet modules. Used at LLR for keeping an rpm repository with the [DPM](http://lcgdm.web.cern.ch/dpm) related puppet modules.

They are not generic, in the sense that the name of the meta-module to update (`sartiran-dpm`) is hardcoded in `update_modules` and my email adress is hardcoded in `puppet2pkg.spec`. But this should be very simple to change or to generalize.

Just put them together in a directory `<rpms dir>`.

Needed: puppet (of course), php (yes! the spec file is made with php... I'm not proud of it but it was the easiest solution), rpmbuild.  

An initialization may be required (not sure)

```
cd `<rpms dir>`
mkdir modules
puppet module --modulepath `<rpms dir>`/modules install <module name>
```

Then it is enough to run periodically

```
`<rpms dir>`/update_modules
```

to have the set of modules updated and the rpms and source rpms (there is probably no difference between the two) created. They will be in the directories `pks` and `spkgs` under `<rpms dir>`.

