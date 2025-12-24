#ifndef CIDESectionEntry_OBJS_H
#define CIDESectionEntry_OBJS_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_OBJS : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	std::string					m_strModelName;
	std::string					m_strTextureName;
	unsigned long				m_uiClumpCount;
	float						m_fDrawDistances[3];
	unsigned long				m_uiFlags;

	unsigned char				m_ucFormatType;
};

#endif