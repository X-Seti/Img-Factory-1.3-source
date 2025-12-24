#ifndef CIDESectionEntry_TOBJ_H
#define CIDESectionEntry_TOBJ_H

#include "CIDESectionEntry.h"
#include <string>
#include <vector>

struct CIDESectionEntry_TOBJ : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	unsigned long				m_uiClumpCount;
	std::vector<float>			m_vecDrawDistances;
	unsigned long				m_uiFlags;
	unsigned long				m_uiTimeOn;
	unsigned long				m_uiTimeOff;

	unsigned long				m_uiTokenCount;
};

#endif