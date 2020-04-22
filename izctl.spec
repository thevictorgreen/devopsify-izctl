Name:           izctl
Version:        1
Release:        11%{?dist}
Summary:        Deploy K8S Cluster

License:        GPL
URL:            http://www.cnn.com
Source0:        izctl-1.tar
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
My K8S Cluster Provisioner

%prep
%setup -q

%build
# nothing to see here

%install
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/local/bin/izctl
/etc/izctl/
/etc/izctl/addons/
/etc/izctl/addons/heapster/
/etc/izctl/addons/heapster/2-heapster.yaml
/etc/izctl/addons/heapster/4-grafana.yaml
/etc/izctl/addons/heapster/1-influxdb.yaml
/etc/izctl/addons/heapster/3-heapster-rbac.yaml
/etc/izctl/addons/ingress-controllers/
/etc/izctl/addons/ingress-controllers/traefik/
/etc/izctl/addons/ingress-controllers/traefik/app/
/etc/izctl/addons/ingress-controllers/traefik/app/app-service-internal.yaml
/etc/izctl/addons/ingress-controllers/traefik/app/tls/
/etc/izctl/addons/ingress-controllers/traefik/app/tls/keypairs/
/etc/izctl/addons/ingress-controllers/traefik/app/tls/keypairs/readme.txt
/etc/izctl/addons/ingress-controllers/traefik/app/tls/create_host_tls.sh
/etc/izctl/addons/ingress-controllers/traefik/app/app-ingress.yaml
/etc/izctl/addons/ingress-controllers/traefik/app/hosts/
/etc/izctl/addons/ingress-controllers/traefik/app/hosts/readme.txt
/etc/izctl/addons/ingress-controllers/traefik/app/app-namespace.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/rbac/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/rbac/traefik-rbac.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/common/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/common/ns-and-sa.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/common/traefik-default-server-secret.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/common/traefik-config.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/deployment/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/deployment/traefik-deployment.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/exec/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/exec/label_node.sh
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/exec/keypairs/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/exec/keypairs/readme.txt
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/exec/create_host_tls.sh
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/service/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/service/traefik-service.yaml
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/haproxy/
/etc/izctl/addons/ingress-controllers/traefik/traefik-ingress-controller/haproxy/haproxy.cfg
/etc/izctl/addons/utils/
/etc/izctl/addons/dashboard/
/etc/izctl/addons/dashboard/dashboard-admin.yaml
/etc/izctl/addons/dashboard/readme.txt
/etc/izctl/addons/dashboard/kubernetes-dashboard.yaml
/etc/izctl/addons/cni/
/etc/izctl/addons/cni/calico/
/etc/izctl/addons/cni/calico/rbac-kdd.yaml
/etc/izctl/addons/cni/calico/calico.yaml
/etc/izctl/conf/
/etc/izctl/conf/keepalived-3-0.conf
/etc/izctl/conf/keepalived-1-1.conf
/etc/izctl/conf/keepalived-4-2.conf
/etc/izctl/conf/kube-2-3.yaml
/etc/izctl/conf/kube-0-2.yaml
/etc/izctl/conf/kube-4-4.yaml
/etc/izctl/conf/etcd-4-4.yaml
/etc/izctl/conf/kube-0-3.yaml
/etc/izctl/conf/etcd-2-2.yaml
/etc/izctl/conf/kube-2-2.yaml
/etc/izctl/conf/keepalived-4-3.conf
/etc/izctl/conf/keepalived-1-0.conf
/etc/izctl/conf/keepalived-3-1.conf
/etc/izctl/conf/etcd-4.ext
/etc/izctl/conf/kube-3-1.yaml
/etc/izctl/conf/etcd-3-1.yaml
/etc/izctl/conf/kube-0-4.yaml
/etc/izctl/conf/etcd-4-3.yaml
/etc/izctl/conf/kube-4-3.yaml
/etc/izctl/conf/kube-1-0.yaml
/etc/izctl/conf/etcd-1-0.yaml
/etc/izctl/conf/keepalived-2-2.conf
/etc/izctl/conf/keepalived-4-4.conf
/etc/izctl/conf/etcd-2.ext
/etc/izctl/conf/etcd-3.ext
/etc/izctl/conf/kube-wnodes
/etc/izctl/conf/etcd-1-1.yaml
/etc/izctl/conf/kube-1-1.yaml
/etc/izctl/conf/etcd-1.ext
/etc/izctl/conf/kube-4-2.yaml
/etc/izctl/conf/etcd-4-2.yaml
/etc/izctl/conf/etcd-3-0.yaml
/etc/izctl/conf/kube-3-0.yaml
/etc/izctl/conf/etcd-0.ext
/etc/izctl/conf/kube-2-4.yaml
/etc/izctl/conf/kube-1-2.yaml
/etc/izctl/conf/kube-4-1.yaml
/etc/izctl/conf/etcd-4-1.yaml
/etc/izctl/conf/etcd-3-3.yaml
/etc/izctl/conf/blank/
/etc/izctl/conf/blank/kube-2-3.yaml
/etc/izctl/conf/blank/kube-0-2.yaml
/etc/izctl/conf/blank/kube-4-4.yaml
/etc/izctl/conf/blank/etcd-4-4.yaml
/etc/izctl/conf/blank/kube-0-3.yaml
/etc/izctl/conf/blank/etcd-2-2.yaml
/etc/izctl/conf/blank/kube-2-2.yaml
/etc/izctl/conf/blank/etcd-4.ext
/etc/izctl/conf/blank/kube-3-1.yaml
/etc/izctl/conf/blank/etcd-3-1.yaml
/etc/izctl/conf/blank/kube-0-4.yaml
/etc/izctl/conf/blank/etcd-4-3.yaml
/etc/izctl/conf/blank/kube-4-3.yaml
/etc/izctl/conf/blank/kube-1-0.yaml
/etc/izctl/conf/blank/etcd-1-0.yaml
/etc/izctl/conf/blank/etcd-2.ext
/etc/izctl/conf/blank/etcd-3.ext
/etc/izctl/conf/blank/kube-wnodes
/etc/izctl/conf/blank/etcd-1-1.yaml
/etc/izctl/conf/blank/kube-1-1.yaml
/etc/izctl/conf/blank/etcd-1.ext
/etc/izctl/conf/blank/kube-4-2.yaml
/etc/izctl/conf/blank/etcd-4-2.yaml
/etc/izctl/conf/blank/etcd-3-0.yaml
/etc/izctl/conf/blank/kube-3-0.yaml
/etc/izctl/conf/blank/etcd-0.ext
/etc/izctl/conf/blank/kube-2-4.yaml
/etc/izctl/conf/blank/kube-1-2.yaml
/etc/izctl/conf/blank/kube-4-1.yaml
/etc/izctl/conf/blank/etcd-4-1.yaml
/etc/izctl/conf/blank/etcd-3-3.yaml
/etc/izctl/conf/blank/kube-3-3.yaml
/etc/izctl/conf/blank/kube-quorum
/etc/izctl/conf/blank/kube-3-2.yaml
/etc/izctl/conf/blank/etcd-3-2.yaml
/etc/izctl/conf/blank/etcd-4-0.yaml
/etc/izctl/conf/blank/kube-4-0.yaml
/etc/izctl/conf/blank/kube-1-3.yaml
/etc/izctl/conf/blank/kube-1-4.yaml
/etc/izctl/conf/blank/etcd-0-0.yaml
/etc/izctl/conf/blank/kube-0-0.yaml
/etc/izctl/conf/blank/etcd-2-1.yaml
/etc/izctl/conf/blank/kube-2-1.yaml
/etc/izctl/conf/blank/etcd-quorum
/etc/izctl/conf/blank/kube-2-0.yaml
/etc/izctl/conf/blank/etcd-2-0.yaml
/etc/izctl/conf/blank/kube-3-4.yaml
/etc/izctl/conf/blank/kube-0-1.yaml
/etc/izctl/conf/kube-3-3.yaml
/etc/izctl/conf/haproxy-4.cfg
/etc/izctl/conf/keepalived-2-0.conf
/etc/izctl/conf/haproxy-1.cfg
/etc/izctl/conf/keepalived-2-1.conf
/etc/izctl/conf/kube-quorum
/etc/izctl/conf/haproxy-0.cfg
/etc/izctl/conf/keepalived-0-0.conf
/etc/izctl/conf/haproxy-2.cfg
/etc/izctl/conf/kube-3-2.yaml
/etc/izctl/conf/etcd-3-2.yaml
/etc/izctl/conf/etcd-4-0.yaml
/etc/izctl/conf/kube-4-0.yaml
/etc/izctl/conf/haproxy-3.cfg
/etc/izctl/conf/kube-1-3.yaml
/etc/izctl/conf/keepalived-4-0.conf
/etc/izctl/conf/keepalived-3-2.conf
/etc/izctl/conf/kube-1-4.yaml
/etc/izctl/conf/etcd-0-0.yaml
/etc/izctl/conf/kube-0-0.yaml
/etc/izctl/conf/etcd-2-1.yaml
/etc/izctl/conf/kube-2-1.yaml
/etc/izctl/conf/etcd-quorum
/etc/izctl/conf/kube-2-0.yaml
/etc/izctl/conf/etcd-2-0.yaml
/etc/izctl/conf/kube-3-4.yaml
/etc/izctl/conf/kube-0-1.yaml
/etc/izctl/conf/keepalived-3-3.conf
/etc/izctl/conf/keepalived-4-1.conf
/var/lib/izctl/
/var/lib/izctl/pki/
/var/lib/izctl/pki/etcd/
/var/lib/izctl/pki/etcd/readme.txt
