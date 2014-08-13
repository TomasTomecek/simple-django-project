PY3_MOCK_CFG=rhscl-python3
SDP_MOCK_CFG=rhscl-python3-sdp
PY3_MOCK_PATH=/var/lib/mock/$(PY3_MOCK_CFG)/result
SDP_MOCK_PATH=/var/lib/mock/$(SDP_MOCK_CFG)/result
DEPLOY_HOST=rhel7-sdp

default: scl-all

help:
	@echo "Usage: make <target>"
	@echo
	@echo "Available targets are:"
	@echo " help                    show this text"
	@echo " clean                   remove temporary files"
	@echo " install                 install program on current system"
	@echo " source                  create source tarball"
	@echo " srpm                    create source rpm"
	@echo " rpm                     build rpm with latest sources"
	@echo " scl-rpm                 build SCL rpm"


clean:
	python setup.py clean
	rm -rf ./*.src.rpm || :
	rm -rf ./*.tar.gz || :
	rm -rf ./*.egg-info || :
	rm ./rpms/* || :

install:
	python setup.py install

source: clean
	python setup.py sdist -d .

srpm: source
	rpmbuild -bs ./*.spec --define "_sourcedir ." --define "_specdir ." --define "_srcrpmdir ."

rpm: srpm
	rpmbuild --rebuild ./*.src.rpm

scl: srpm
	mock --verbose --root=$(SDP_MOCK_CFG) ./*.src.rpm
	mkdir -p rpms/app/
	rm -f rpms/app/*
	cp -av $(SDP_MOCK_PATH)/*.noarch.rpm rpms/app/

sdp:
	$(MAKE) -C scl/ repo-scl
	mkdir -p rpms/scl/
	rm -f rpms/scl/*
	cp -av $(PY3_MOCK_PATH)/sdp-*.noarch.rpm rpms/scl/

devel-conf:
	$(MAKE) -C conf/devel scl-rpm
	mkdir -p rpms/conf/
	rm -f rpms/conf/*
	cp -av $(SDP_MOCK_PATH)/sdp-*.noarch.rpm rpms/scl/

scl-all: sdp scl devel-conf

deploy:
	ansible-playbook ansible.yml

quick: scl devel-conf deploy

