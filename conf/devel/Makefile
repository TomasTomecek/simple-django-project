MOCK_CONFIG=rhscl-python3-sdp

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
	rm -rf ./*.rpm

srpm:
	rpmbuild -bs ./*.spec --define "_sourcedir ." --define "_specdir ." --define "_srcrpmdir ."

rpm: srpm
	rpmbuild --rebuild ./*.src.rpm

scl-rpm: srpm
	mock --verbose --root=$(MOCK_CONFIG) --rebuild ./*.src.rpm

