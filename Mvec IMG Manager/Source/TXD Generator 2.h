
// GTA Tools GUI.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CGTAToolsGUIApp:
// See GTA Tools GUI.cpp for the implementation of this class
//

class CGTAToolsGUIApp : public CWinApp
{
public:
	CGTAToolsGUIApp();

// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CGTAToolsGUIApp theApp;