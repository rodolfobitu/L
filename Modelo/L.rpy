I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID d589d57d-f57b-4f70-b35b-cf156cf1ceeb;
	- _myState = 8192;
	- _name = "L";
	- _objectCreation = "513273075220150-10431151";
	- _umlDependencyID = "1639";
	- _lastID = 19;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "RequisitosPKG.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "RequisitosPKG";
		- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID a6411594-1cb9-4a7d-b0e7-22b0209f1dfe;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 13;
		- value = 
		{ ISubsystem 
			- fileName = "RequisitosPKG";
			- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
		}
		{ ISubsystem 
			- fileName = "Adc";
			- _id = GUID 4e48f159-95db-45fc-93e1-eb52ffa8a574;
		}
		{ ISubsystem 
			- fileName = "ES770";
			- _id = GUID a719ac8d-1468-4d24-9af1-6ea3915beef4;
		}
		{ ISubsystem 
			- fileName = "Main";
			- _id = GUID 97014e96-fef5-4d72-a0bf-e169ad6602da;
		}
		{ ISubsystem 
			- fileName = "Calibrate";
			- _id = GUID de1916b9-abbb-4a5b-ac4b-8d37ecc3815f;
		}
		{ ISubsystem 
			- fileName = "Pwm";
			- _id = GUID 969b7009-3a30-4e9c-9e61-cc6067cc654c;
		}
		{ ISubsystem 
			- fileName = "VelocityCorrection";
			- _id = GUID f09c62c6-0cf4-43c8-8482-e5533a35acd1;
		}
		{ ISubsystem 
			- fileName = "PID";
			- _id = GUID 17b532b4-5d12-43b0-8ea4-bde137f4d26d;
		}
		{ ISubsystem 
			- fileName = "Timer0";
			- _id = GUID 04e6c567-266f-4d80-b008-585656f86c8f;
		}
		{ ISubsystem 
			- fileName = "Util";
			- _id = GUID dcae37ac-4265-4e42-aef5-3b8bd3ec64be;
		}
		{ ISubsystem 
			- fileName = "Position";
			- _id = GUID b6b8f617-3b56-4215-899e-c50d2b4cdf54;
		}
		{ ISubsystem 
			- fileName = "PwmControl";
			- _id = GUID be6190aa-abf0-4186-a21e-9d3d1314b634;
		}
		{ ISubsystem 
			- fileName = "VelocityControl";
			- _id = GUID 9ef66e9b-63c1-4374-9980-9db6a2415c36;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ IDiagram 
			- _id = GUID da1307e5-60c9-4a8f-aeb8-e22cf2e3bb6c;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Requirement";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,84,96";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,207";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "225,225,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Diagrama de Requisitos";
			- _objectCreation = "513273275220150-10451151";
			- _umlDependencyID = "3638";
			- _lastID = 1;
			- _lastModifiedTime = "11.7.2015::2:51:59";
			- _graphicChart = { CGIClassChart 
				- _id = GUID c1de5502-36ee-46c5-871e-8bcfcccb8878;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID da1307e5-60c9-4a8f-aeb8-e22cf2e3bb6c;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 12;
				{ CGIClass 
					- _id = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 969ef191-6726-4cee-a403-273b77fd63b2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAnnotation 
					- _id = GUID 6aac85c6-2cd5-4705-a1aa-8f12823df2b7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R1";
						- _id = GUID 556bfa1d-8681-46c4-b94a-40015c804034;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.125623 0 0 0.0787153 95.0481 135.325 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID b4748670-8b4d-4c21-b115-c1be0613a128;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R2";
						- _id = GUID 8ab28847-c904-42a8-be01-f9a42e8ef33d;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.139299 0 0 0.0815018 268.999 131.305 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID c519febb-fdbb-458c-9218-26602d3a3646;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R3";
						- _id = GUID 7596df2d-95f6-4acd-8f1a-8f8044b4f692;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.142989 0 0 0.096154 462.999 132.135 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 60c22a26-06e6-409f-ac17-b31aef7b3b37;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R4a";
						- _id = GUID ecadc152-43f5-4f5f-aee2-ebb97033eb3d;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.115314 0 0 0.0879123 672 133.272 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 8cfa9988-367e-491d-aaa2-e34f0677d12b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R4b";
						- _id = GUID 1b3f28b7-c544-4d64-b190-15f8f03d0849;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.118081 0 0 0.0915753 94.9998 284.145 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 46d61150-0ea2-4c84-9c22-5aeba4317898;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R4c";
						- _id = GUID d8a7f5ea-0eee-4e98-8538-1217e6ffc527;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.122693 0 0 0.0989014 277 270.053 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 013b0b6f-3d74-4f57-81fd-d1fd4c5ea134;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R5a";
						- _id = GUID 3a5e3be5-f873-48f1-973b-50a14e4fe020;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.102399 0 0 0.114469 477 267.973 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 72edc09f-603e-4389-a000-bb6e270c3aff;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R5b";
						- _id = GUID 11234076-4b60-4eb5-8d55-5b0f2469b0f7;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.109778 0 0 0.10989 670.999 265.983 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID df4f5bea-06e6-47b9-8204-b5bf8d3b6532;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R5c";
						- _id = GUID 625035c6-b8cb-4393-8150-8c439f95ef19;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.105166 0 0 0.0750914 191 457.064 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID fc12fb43-eb7a-42a2-b28e-7c225145593c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R6a";
						- _id = GUID 3b81d61f-0ac3-4682-af07-e92581e0aaeb;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133764 0 0 0.0924909 336 443.024 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIAnnotation 
					- _id = GUID 4596f3f3-94eb-4d9f-abaa-c6905cdc30da;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 176;
					- m_pModelObject = { IHandle 
						- _m2Class = "IRequirement";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "R6b";
						- _id = GUID 1a376cd2-d6a6-43f5-998e-5664150cf01e;
					}
					- m_pParent = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.133102 0 0 0.0970696 549 449.993 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1095  1084 1095  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 7aaa048d-2727-4e32-b490-b82c02d69df0;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "RequisitosPKG.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "RequisitosPKG";
				- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
			}
		}
		{ IDiagram 
			- _id = GUID 62f562ae-a76e-4711-b5ac-2d722bfe4dda;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline@Child.NameCompartment@Name";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Diagrama de defini\ç\ão de blocos";
			- _objectCreation = "513273475220150-10471151";
			- _umlDependencyID = "4139";
			- _lastModifiedTime = "11.7.2015::2:52:29";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 4466841c-19fb-416a-ac33-f8dcae28233e;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 62f562ae-a76e-4711-b5ac-2d722bfe4dda;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 20;
				{ CGIClass 
					- _id = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 969ef191-6726-4cee-a403-273b77fd63b2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID bb8f4afa-b9f0-474d-a297-445d2a889c90;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "PID.sbs";
						- _subsystem = "PID";
						- _class = "";
						- _name = "PID";
						- _id = GUID 3305f741-356c-4257-8c0d-fa742d2005f4;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "PID::PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.359773 0 0 0.114973 29.2805 742.174 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PID.sbs";
							- _subsystem = "PID";
							- _class = "PID";
							- _name = "pid_init(float,float,float,float,float)";
							- _id = GUID bfbf84ac-35f9-4272-a12c-109eb7b04d20;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PID.sbs";
							- _subsystem = "PID";
							- _class = "PID";
							- _name = "pid_update(pid,float,float)";
							- _id = GUID c01636b7-299f-46dd-92cb-92a08f66af86;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 69799352-29c7-40dc-98b2-97a1a5f2574b;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "VelocityCorrection.sbs";
						- _subsystem = "VelocityCorrection";
						- _class = "";
						- _name = "Velocity";
						- _id = GUID 8f3ace1e-00be-4cd5-81a6-ff83ec3a4084;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "VelocityCorrection::Velocity";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.229462 0 0 0.102496 26.5411 427.279 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "VelocityCorrection.sbs";
							- _subsystem = "VelocityCorrection";
							- _class = "Velocity";
							- _name = "iSamplesRight";
							- _id = GUID 8f830882-0463-4e80-b380-f03a7e5a9881;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "VelocityCorrection.sbs";
							- _subsystem = "VelocityCorrection";
							- _class = "Velocity";
							- _name = "iSamplesLeft";
							- _id = GUID d63063c8-73f4-4b5e-b247-71093e99ac8f;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "VelocityCorrection.sbs";
							- _subsystem = "VelocityCorrection";
							- _class = "Velocity";
							- _name = "velocity_task()";
							- _id = GUID 96aae243-9aad-45bf-b42c-d56ec46a399a;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "VelocityCorrection.sbs";
							- _subsystem = "VelocityCorrection";
							- _class = "Velocity";
							- _name = "velocity_calcSpeed(int*)";
							- _id = GUID d30d8b77-f934-4df3-92ce-75fe8f77d167;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID a521603d-2ebc-4243-9398-e90087efe1b1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "VelocityCorrection.sbs";
						- _subsystem = "VelocityCorrection";
						- _class = "Velocity";
						- _name = "PID";
						- _id = GUID 85493d02-a1cc-4ebb-8ebc-5d3155ca13c4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 69799352-29c7-40dc-98b2-97a1a5f2574b;
					- m_sourceType = 'F';
					- m_pTarget = GUID bb8f4afa-b9f0-474d-a297-445d2a889c90;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 281 1080 ;
					- m_TargetPort = 172 329 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 7a830839-0bd0-4a14-859e-12fb5a2febff;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Adc.sbs";
						- _subsystem = "Adc";
						- _class = "";
						- _name = "ADC";
						- _id = GUID ba041dbb-0476-4ff5-b43b-4f55f264ad83;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Adc::ADC";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.285175 0 0 0.15508 986.43 353.979 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=34%,66%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "adc_init()";
							- _id = GUID 83ab65e6-3bea-4c1c-8cb0-156541d4ca49;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "adc_get()";
							- _id = GUID 89725dbb-1972-41a6-acb7-e0917997de89;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "turnOnLed(char)";
							- _id = GUID 7d6d5230-4f2c-482e-94ab-956250a17a39;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 1af8babc-7863-403d-948c-54cf5ca2049c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Calibrate.sbs";
						- _subsystem = "Calibrate";
						- _class = "";
						- _name = "Calibrate";
						- _id = GUID be320102-be73-4e44-8312-fd0a2fd307e0;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Calibrate::Calibrate";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.157696 0 0 0.106061 562.685 603.106 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=23%,77%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Calibrate.sbs";
							- _subsystem = "Calibrate";
							- _class = "Calibrate";
							- _name = "calibrate_run()";
							- _id = GUID 08352d71-e1a6-4cd6-88d9-f03d7ddafcfe;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Calibrate.sbs";
							- _subsystem = "Calibrate";
							- _class = "Calibrate";
							- _name = "calibrate_runMock()";
							- _id = GUID 349dfb3e-243f-4e05-a7ad-8404b70674d3;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID dd8ccc31-76fc-473c-b468-7da9beb29dc8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Calibrate.sbs";
						- _subsystem = "Calibrate";
						- _class = "Calibrate";
						- _name = "ADC";
						- _id = GUID 4708b142-1ee6-4ba6-bcbf-d692305d0936;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "ADC";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1af8babc-7863-403d-948c-54cf5ca2049c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7a830839-0bd0-4a14-859e-12fb5a2febff;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 776 658 ;
					- m_TargetPort = 726 1206 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 82ddd08e-c3b1-4a06-a329-88804f13eba0;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "ES770.sbs";
						- _subsystem = "ES770";
						- _class = "";
						- _name = "ES770";
						- _id = GUID 99593ef1-5d97-4bf0-a6dd-46529409f792;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "ES770::ES770";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.135977 0 0 0.105169 43.728 245.399 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 0c369014-6b30-4e6f-bd0b-1b82e2644372;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Pwm.sbs";
						- _subsystem = "Pwm";
						- _class = "";
						- _name = "PWM";
						- _id = GUID bc9fea5c-f7f4-4f35-9575-dd8326993a4e;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Pwm::PWM";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.422096 0 0 0.146168 866.156 678.911 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Pwm.sbs";
							- _subsystem = "Pwm";
							- _class = "PWM";
							- _name = "pwm_init(pwmDevice)";
							- _id = GUID 4f51c010-ca30-4ae8-a1f4-ad386e73cc89;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Pwm.sbs";
							- _subsystem = "Pwm";
							- _class = "PWM";
							- _name = "pwm_setDutyCycle(pwmDevice,unsigned int)";
							- _id = GUID 68012f6f-0b85-4746-80eb-bb8300b54d8c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Pwm.sbs";
							- _subsystem = "Pwm";
							- _class = "PWM";
							- _name = "pwm_setDirection(pwmDevice,char)";
							- _id = GUID c02384ac-8812-49e2-84bb-dc2ad8a35345;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 080f7f84-0f45-4299-9568-c2c33ea61748;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Calibrate.sbs";
						- _subsystem = "Calibrate";
						- _class = "Calibrate";
						- _name = "PWM";
						- _id = GUID effa93a1-bf60-467e-86b7-b06a9c1eb4dc;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "PWM";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1af8babc-7863-403d-948c-54cf5ca2049c;
					- m_sourceType = 'F';
					- m_pTarget = GUID 0c369014-6b30-4e6f-bd0b-1b82e2644372;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 896 1267 ;
					- m_TargetPort = 928 534 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "";
						- _name = "L";
						- _id = GUID fff3c873-da27-426a-80e1-007c81521709;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Main::L";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.155807 0 0 0.305704 393.688 129.423 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=55%,45%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 9;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "uiTimer0_endPeriod";
							- _id = GUID a7189b78-8eee-40f3-99a4-1e2538ad9164;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "uiLeftCounter";
							- _id = GUID 760e68a0-17d5-449e-8149-9d32d8e27cad;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "uiRightCounter";
							- _id = GUID 4676ad87-1f83-4fe3-8588-cd23ffdaf29c;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "fLeftReference";
							- _id = GUID 9c0aa73c-8b3f-424a-960a-c1a9d592a52d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "fRightReference";
							- _id = GUID 02be417c-fa6c-4196-8f26-2e27e04babc9;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "fLeftSpeed";
							- _id = GUID 097ece71-6073-4945-bc46-2df5e8db6a6d;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "fRightSpeed";
							- _id = GUID 97e73868-72ba-4dab-8f80-9cab95818e71;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "uiSensorLimits";
							- _id = GUID d1bda750-2fe0-4f95-b7cf-3a272c0b63d1;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "fPosition";
							- _id = GUID 977373c5-e006-431a-9d18-bf1c652d1b36;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "main()";
							- _id = GUID 099af860-d138-40c3-91de-e7bb75704156;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "isr_CyclicExecutive()";
							- _id = GUID 943bad8b-caee-4d29-8f57-6ab66c6df376;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "L";
							- _name = "L_init()";
							- _id = GUID 47d0a09c-a3f7-409b-a618-ac5099b9f612;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID dcdc87c1-3acf-49c5-bb47-9f67b4478c23;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "L";
						- _name = "ES770";
						- _id = GUID fc6123f7-25c5-494d-87bd-35156183aaf2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "ES770";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 82ddd08e-c3b1-4a06-a329-88804f13eba0;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 471 763 ;
					- m_TargetPort = 465 1033 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID ca0df77d-ee9d-4e9f-ab13-b39a7c0e4a4e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "L";
						- _name = "ADC";
						- _id = GUID 141ca2d9-7037-4817-9856-b157bad1b502;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "ADC";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7a830839-0bd0-4a14-859e-12fb5a2febff;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 830 795 ;
					- m_TargetPort = 227 542 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 1eeb38cc-604c-460d-94a2-214f0281691f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "L";
						- _name = "Calibrate";
						- _id = GUID 2e59b623-f8d6-4815-bb45-1f08d5b3fe82;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Calibrate";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1af8babc-7863-403d-948c-54cf5ca2049c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 990 1356 ;
					- m_TargetPort = 459 931 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 0e3d8851-3c06-404d-96f4-c6814890e4fb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "L";
						- _name = "Velocity";
						- _id = GUID 51cea3f5-0955-4ef3-8978-b65921bc2acb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "VelocityCorrection";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- m_sourceType = 'F';
					- m_pTarget = GUID 69799352-29c7-40dc-98b2-97a1a5f2574b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 259 1419 ;
					- m_TargetPort = 704 797 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 13d4110d-67c6-4114-8738-3b3a7b4e9399;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Timer0.sbs";
						- _subsystem = "Timer0";
						- _class = "";
						- _name = "Timer0";
						- _id = GUID 0d847196-51a4-4cbf-b589-78dc9652ab81;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Timer0::Timer0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.175637 0 0 0.151515 66.6488 -19.8485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=37%,63%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "cResetValueHigh";
							- _id = GUID 7d2285d2-4d8e-4667-b203-f95292e75d98;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "cResetValueLow";
							- _id = GUID 3092e58f-2117-4ad6-8e41-d28a643301f5;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "timer0_init()";
							- _id = GUID 7788a61a-e5fc-453f-aef6-a5cedf232dd7;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "timer0_config(unsigned int)";
							- _id = GUID 2e7f4590-5772-4c18-9e7f-286153ac5250;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "timer0_reset()";
							- _id = GUID 943688d1-084d-4892-a8b0-a106217d1050;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Timer0.sbs";
							- _subsystem = "Timer0";
							- _class = "Timer0";
							- _name = "timer0_timeLeft()";
							- _id = GUID be8e99ed-82b1-433f-aef3-1f6eb9eef644;
						}
					}
				}
				{ CGIClass 
					- _id = GUID b2129c5b-2f64-4f94-be8c-ef1490d4ae3d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Util.sbs";
						- _subsystem = "Util";
						- _class = "";
						- _name = "util";
						- _id = GUID 6ffc0103-5de0-4bf2-8c20-224fa6031c93;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Util::util";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2088;
					- m_transform = 0.172805 0 0 0.101604 251.654 568.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=14%,86%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "util_genDelay1MS(char)";
							- _id = GUID ab8c95da-be71-472a-84cb-0ee9ce50078e;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "util_genDelay10MS(char)";
							- _id = GUID 4be3ea06-7d32-4f3b-8483-8f245755086f;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Util.sbs";
							- _subsystem = "Util";
							- _class = "util";
							- _name = "util_genDelay100MS(char)";
							- _id = GUID b0b75084-005c-40a5-b904-6b193eb79f6f;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 55621830-a698-4241-aeb2-d5aed2394fa0;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Position.sbs";
						- _subsystem = "Position";
						- _class = "";
						- _name = "Position";
						- _id = GUID dea1284b-4adc-4f64-8f80-6e4e6dcda9d9;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Position::Position";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.117092 0 0 0.101604 109.766 593.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Position.sbs";
							- _subsystem = "Position";
							- _class = "Position";
							- _name = "position_task()";
							- _id = GUID 7450d44c-0869-476d-a1a7-d8901743218f;
						}
					}
				}
				{ CGIClass 
					- _id = GUID e6d901ff-0043-4f88-b532-2bced64100b7;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "PwmControl.sbs";
						- _subsystem = "PwmControl";
						- _class = "";
						- _name = "PwmControl";
						- _id = GUID 2b24a163-d7b5-423c-b1c2-460c29ba4c11;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "PwmControl::PwmControl";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.166195 0 0 0.101604 665.668 215.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PwmControl.sbs";
							- _subsystem = "PwmControl";
							- _class = "PwmControl";
							- _name = "pwmControl_task()";
							- _id = GUID 8163b9ec-edd9-4326-861b-6da08bfa1d62;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PwmControl.sbs";
							- _subsystem = "PwmControl";
							- _class = "PwmControl";
							- _name = "pwmControl_init()";
							- _id = GUID 19889436-d025-4bad-aca1-3519a8d3f5a1;
						}
					}
				}
				{ CGIClass 
					- _id = GUID d954fa55-b34e-49e5-82bc-955005fe523f;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "VelocityControl.sbs";
						- _subsystem = "VelocityControl";
						- _class = "";
						- _name = "VelocityControl";
						- _id = GUID 2074305a-6607-4850-8af6-8065ecb78ac2;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "VelocityControl::VelocityControl";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.20491 0 0 0.101604 664.59 424.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "VelocityControl.sbs";
							- _subsystem = "VelocityControl";
							- _class = "VelocityControl";
							- _name = "pid";
							- _id = GUID 6b7a3edf-0344-4260-836c-c04350b5b96c;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "VelocityControl.sbs";
							- _subsystem = "VelocityControl";
							- _class = "VelocityControl";
							- _name = "velocityControl_task()";
							- _id = GUID 72731d92-4de4-43e3-9a33-6197b6c56ea9;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "VelocityControl.sbs";
							- _subsystem = "VelocityControl";
							- _class = "VelocityControl";
							- _name = "velocityControl_init()";
							- _id = GUID b57ef153-63d8-4519-aabc-7b48db4c1a44;
						}
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "RequisitosPKG.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "RequisitosPKG";
				- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
			}
		}
		{ IDiagram 
			- _id = GUID 8275f54a-8c8b-48f5-b7d4-66afd5827e9f;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Diagrama de Pacotes";
			- _objectCreation = "513273675220150-10491151";
			- _umlDependencyID = "3285";
			- _lastModifiedTime = "11.7.2015::2:51:59";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 8acbff9e-a8f4-4d74-912c-c229e94dcc5c;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 8275f54a-8c8b-48f5-b7d4-66afd5827e9f;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 8;
				{ CGIClass 
					- _id = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "RequisitosPKG.sbs";
						- _subsystem = "RequisitosPKG";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 969ef191-6726-4cee-a403-273b77fd63b2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID 5f33d284-c2d5-44a5-8a4a-b0a63dd9c299;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Adc.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Adc";
						- _id = GUID 4e48f159-95db-45fc-93e1-eb52ffa8a574;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Adc";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.129112 0 0 0.112076 102 285 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID d27a0eae-cdcd-41ff-8b43-36ee6845beac;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "ES770.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "ES770";
						- _id = GUID a719ac8d-1468-4d24-9af1-6ea3915beef4;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "ES770";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.191612 0 0 0.147698 82 72 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID f7b926eb-6fc9-4466-bf3c-51aa6e17f7e5;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Main.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Main";
						- _id = GUID 97014e96-fef5-4d72-a0bf-e169ad6602da;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Main";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.11102 0 0 0.125977 384 60 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 6357bee0-efdf-4fd9-9aad-24a2bb7a9b8c;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Calibrate.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Calibrate";
						- _id = GUID de1916b9-abbb-4a5b-ac4b-8d37ecc3815f;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Calibrate";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.0690789 0 0 0.0451781 120 456 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 3b3c15f0-d662-4d71-80f3-eb42aac448df;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Pwm.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Pwm";
						- _id = GUID 969b7009-3a30-4e9c-9e61-cc6067cc654c;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Pwm";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.185855 0 0 0.122502 108 588 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID 117d7e8f-a76b-4a15-882a-3323ef8f5bf2;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "VelocityCorrection.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "VelocityCorrection";
						- _id = GUID f09c62c6-0cf4-43c8-8482-e5533a35acd1;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "VelocityCorrection";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.106908 0 0 0.0529974 384 792 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIPackage 
					- _id = GUID b8c889b7-4d3c-4034-b6d1-be26a990f950;
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "PID.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "PID";
						- _id = GUID 17b532b4-5d12-43b0-8ea4-bde137f4d26d;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "PID";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.111842 0 0 0.0599479 120 912 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "RequisitosPKG.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "RequisitosPKG";
				- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID a6411594-1cb9-4a7d-b0e7-22b0209f1dfe;
		}
	}
}

