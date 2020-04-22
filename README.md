# Devopsify-Izctl
Deploys A Highly Available K8S Cluster in Cloud or On-Prem

### Installing
sudo rpm -ivh binary/centos7/izctl-1-11.el7.x86_64.rpm

#### Building
sudo yum install -y gcc rpm-build rpm-devel rpmlint make python bash coreutils diffutils patch rpmdevtools git vim
rpmdev-setuptree
mv izctl-1.tar rpmbuild/SOURCES
mv izctl.spec rpmbuild/SPEC
rpmlint rpmbuild/SPEC/izctl.spec
rpmbuild -ba rpmbuild/SPEC/izctl.spec
rpmlint rpmbuild/RPMS/x86_64/izctl-1-11.el7.x86_64.rpm
sudo rpm -ivh rpmbuild/RPMS/x86_64/izctl-1-11.el7.x86_64.rpm

#### Dependencies
kubeadm 1.11
kubectl 1.11

#### Binary Dependencies
Place the following files in /usr/local/bin
istioctl
helm
etdctl
