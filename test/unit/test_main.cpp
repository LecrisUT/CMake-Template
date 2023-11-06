#include <functional>
#include <iostream>
#include <sstream>

#include <template.h>
#include <catch2/catch_test_macros.hpp>

class AutoRestoreRdbuf {
    std::ostream& out;
    std::streambuf* old;

   public:
    ~AutoRestoreRdbuf() {
        out.rdbuf(old);
    }
    AutoRestoreRdbuf(const AutoRestoreRdbuf&) = delete;
    AutoRestoreRdbuf(AutoRestoreRdbuf&&) = delete;

    AutoRestoreRdbuf(std::ostream& out) : out{out}, old{out.rdbuf()} {}
};

std::string stringWrittentToStream(std::function<void()> f,
                                   std::ostream& out = std::cout) {
    AutoRestoreRdbuf restore{std::cout};
    std::ostringstream oss;
    std::cout.rdbuf(oss.rdbuf());
    f();
    return oss.str();
}

TEST_CASE("Test hello function", "[unit]") {
    auto output = stringWrittentToStream(&tmpl::hello);
    CHECK(output == "Hello, World!\n");
}
