#ifndef CIDESectionEntry_WEAP_H
#define CIDESectionEntry_WEAP_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_WEAP : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	std::string					m_strAnimationName;
	unsigned long				m_uiClumpCount;
	float						m_fDrawDistance;
	unsigned long				m_uiFlags;
};

#endif