from conans import ConanFile, CMake


class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.2.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of cxxopts here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "use_pic": [True, False]
    }
    default_options = {"shared": False, "use_pic": False}
    generators = "cmake"
    exports_sources = "*"
    no_copy_source = True

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_SHARED_LIBS'] = self.options.shared
        cmake.definitions['BUILD_TESTING'] = False
        cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.use_pic
        cmake.definitions['CXXOPTS_BUILD_EXAMPLES'] = False
        cmake.definitions['CXXOPTS_BUILD_TESTS'] = False
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.info.header_only()
