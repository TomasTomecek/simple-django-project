REPO_PATH=/var/tmp/yumrepos/sdp
MOCK_CONFIG=rhscl-python3

default: scl

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
	rm -rf ./*.src.rpm || :

srpm: clean
	rpmbuild -bs ./*.spec --define "_sourcedir ." --define "_specdir ." --define "_srcrpmdir ."

scl: srpm
	mock --verbose --root=$(MOCK_CONFIG) --rebuild ./*.src.rpm

repo-scl: scl
	mkdir -p $(REPO_PATH)
	rm -rf $(REPO_PATH)/*
	cp -av /var/lib/mock/$(MOCK_CONFIG)/result/sdp-*.noarch.rpm $(REPO_PATH)/
	createrepo $(REPO_PATH)/

rpm: srpm
	rpmbuild --rebuild ./*.src.rpm

