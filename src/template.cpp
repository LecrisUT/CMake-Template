#include <iostream>

#include <fmt/core.h>

#include "template.h"

void tmpl::hello() {
    std::cout << fmt::format("Hello, {}!", "World") << std::endl;
}
