#include "Design/Components/Component.hpp"

Component::~Component() {
    for (size_t ii = 0; ii < child_components.size(); ii++) {
        // delete child components
    }
}