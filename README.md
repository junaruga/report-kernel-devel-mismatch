# report-kernel-devel-mismatch

Create SRPM for rawhide.

```
$ fedpkg --release rawhide srpm
```

Run scratch build.

```
$ koji build --scratch --nowait rawhide *.src.rpm
```
