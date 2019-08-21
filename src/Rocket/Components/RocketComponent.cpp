#include "Rocket/Components/RocketComponent.hpp"

RocketComponent::~RocketComponent() {
    for (size_t ii = 0; ii < child_components.size(); ii++) {
        // delete child components
    }
}