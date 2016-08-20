#pragma once

#include <functional>
#include <glm/gtc/random.hpp>

#include <core/scenemgr.h>
#include <core/transform.h>
#include <core/animation.h>
#include <core/flappyapp.h>
#include <core/entitymgr.h>
#include <core/inputmgr.h>
#include <core/gamemgr.h>
#include <ui/button.h>

#include "ballctrl.h"
#include "basketctrl.h"
#include "gamectrl.h"

namespace game {

class MyGameMgr : public flappy::GameMgr
{
public:
    void init() override;
private:
    void createBasket(std::string spritePath, glm::vec2 pos);
};

} // game
