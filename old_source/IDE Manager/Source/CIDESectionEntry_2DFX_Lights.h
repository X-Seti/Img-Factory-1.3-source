#ifndef CIDESectionEntry_2DFX_Lights_H
#define CIDESectionEntry_2DFX_Lights_H

#include "CIDESectionEntry.h"
#include <string>

struct CIDESectionEntry_2DFX_Lights : public CIDESectionEntry
{
	unsigned long				m_uiObjectId;
	float						m_fPosition[3];
	unsigned char				m_ucColour[3];
	unsigned long				m_uiUnknown1;
	unsigned long				m_ui2dfxType;
	std::string					m_strCoronaTexture;
	std::string					m_strShadowTexture;
	float						m_fViewDistance;
	float						m_fOuterRange;
	float						m_fCoronaSize;
	float						m_fInnerRange;
	unsigned long				m_uiIDEFlag;
	unsigned long				m_uiFlash;
	unsigned long				m_uiWet;
	unsigned long				m_uiFlare;
	unsigned long				m_uiDust;
};

#endif