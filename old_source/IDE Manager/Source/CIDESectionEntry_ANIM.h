#ifndef CIDESectionEntry_ANIM_H
#define CIDESectionEntry_ANIM_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_ANIM : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	std::string					m_strAnimationName;
	float						m_fDrawDistance;
	unsigned long				m_uiFlags;
};

#endif