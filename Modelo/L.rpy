I-Logix-RPY-Archive version 8.5.2 Modeler C++ 1159120
{ IProject 
	- _id = GUID d589d57d-f57b-4f70-b35b-cf156cf1ceeb;
	- _myState = 8192;
	- _name = "L";
	- _objectCreation = "5110896212920152026006851";
	- _umlDependencyID = "1713";
	- _lastID = 14;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID c8db5a9c-23d1-4ddf-bb1b-e2195780afba;
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
			- fileName = "Default";
			- _id = GUID c8db5a9c-23d1-4ddf-bb1b-e2195780afba;
		}
		{ ISubsystem 
			- fileName = "RequisitosPKG";
			- _id = GUID 17add19b-97c5-4df4-8f43-59f8e104953b;
		}
		{ ISubsystem 
			- fileName = "ES770";
			- _id = GUID a719ac8d-1468-4d24-9af1-6ea3915beef4;
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
			- fileName = "Encoder";
			- _id = GUID 68038364-716f-447b-98ff-da4c40d2d83e;
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
			- fileName = "SelfTest";
			- _id = GUID eab1f781-5284-4f96-8edd-7271be1637c3;
		}
		{ ISubsystem 
			- fileName = "SensorBar";
			- _id = GUID 71e10367-4efc-4e82-960e-9f02755cec47;
		}
		{ ISubsystem 
			- fileName = "Adc";
			- _id = GUID 4e48f159-95db-45fc-93e1-eb52ffa8a574;
		}
		{ ISubsystem 
			- fileName = "Main";
			- _id = GUID 97014e96-fef5-4d72-a0bf-e169ad6602da;
		}
		{ ISubsystem 
			- fileName = "Motor";
			- _id = GUID ff7b1e3e-7cc3-4f55-9636-78da1b858107;
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
			- _objectCreation = "5110898212920152026004851";
			- _umlDependencyID = "3708";
			- _lastID = 1;
			- _lastModifiedTime = "8.21.2015::4:4:4";
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
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID d281e7c6-9220-4127-9a6c-3c98a8958ff2;
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
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID c8db5a9c-23d1-4ddf-bb1b-e2195780afba;
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
			- _objectCreation = "5110900212920152026002851";
			- _umlDependencyID = "4187";
			- _lastModifiedTime = "8.21.2015::23:29:13";
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
				- elementList = 31;
				{ CGIClass 
					- _id = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID d281e7c6-9220-4127-9a6c-3c98a8958ff2;
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
					- _id = GUID 82b51846-4320-493f-a573-067eb5131bc4;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "SensorBar.sbs";
						- _subsystem = "SensorBar";
						- _class = "";
						- _name = "SensorBar";
						- _id = GUID 6d97aadf-77fb-4771-aa28-f411662c98d4;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "SensorBar::SensorBar";
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
					- m_transform = 0.346553 0 0 0.108734 702.307 191.226 ;
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
					- frameset = "<frameset rows=47%,53%>
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
							- _filename = "SensorBar.sbs";
							- _subsystem = "SensorBar";
							- _class = "SensorBar";
							- _name = "vSensorTask()";
							- _id = GUID 90cc5a46-b09c-4201-a390-261b40464382;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "SensorBar.sbs";
							- _subsystem = "SensorBar";
							- _class = "SensorBar";
							- _name = "cSensorBarSpline(*char,char)";
							- _id = GUID 6e0dc10e-32f8-49a1-9507-cccbd4a361fc;
						}
					}
				}
				{ CGIClass 
					- _id = GUID 275d7a3e-c980-41d4-9600-cb91b36dda72;
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
						- _filename = "Encoder.sbs";
						- _subsystem = "Encoder";
						- _class = "";
						- _name = "Encoder";
						- _id = GUID 992ef8c4-c3de-42a8-a1d9-fa269333e430;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Encoder::Encoder";
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
					- m_transform = 0.2644 0 0 0.127451 94.4713 10.0686 ;
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
							- _filename = "Encoder.sbs";
							- _subsystem = "Encoder";
							- _class = "Encoder";
							- _name = "vEncoderTask(*void)";
							- _id = GUID 19772ffa-8659-48d7-961e-7be0fbde93e1;
						}
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
							- _name = "pidPidInit(double,double,double)";
							- _id = GUID bfbf84ac-35f9-4272-a12c-109eb7b04d20;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "PID.sbs";
							- _subsystem = "PID";
							- _class = "PID";
							- _name = "dPidUpdate(pid,double)";
							- _id = GUID c01636b7-299f-46dd-92cb-92a08f66af86;
						}
					}
				}
				{ CGIClass 
					- _id = GUID fd999fbb-bade-4a45-9c1c-ef6f57aca4bc;
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
						- _filename = "Motor.sbs";
						- _subsystem = "Motor";
						- _class = "";
						- _name = "Motor";
						- _id = GUID 562534d4-2a40-425c-b8de-21781bcc10bd;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Motor::Motor";
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
					- m_transform = 0.314448 0 0 0.0944742 460.372 758.918 ;
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
					- frameset = "<frameset rows=45%,55%>
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
							- _filename = "Motor.sbs";
							- _subsystem = "Motor";
							- _class = "Motor";
							- _name = "vMotorTask(*void)";
							- _id = GUID 54d89192-32fa-4222-b4db-0bf2e2dc99ce;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID d3a6ecec-78f0-437f-9216-8035fe5187b7;
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
						- _filename = "Motor.sbs";
						- _subsystem = "Motor";
						- _class = "Motor";
						- _name = "PID";
						- _id = GUID 6c9f2051-44b3-4eb6-ac1d-7d2ec9bb87ce;
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
					- m_pSource = GUID fd999fbb-bade-4a45-9c1c-ef6f57aca4bc;
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
					- m_SourcePort = 985 858 ;
					- m_TargetPort = 1047 894 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 69799352-29c7-40dc-98b2-97a1a5f2574b;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "VelocityCorrection.sbs";
						- _subsystem = "VelocityCorrection";
						- _class = "";
						- _name = "VelocityCorrection";
						- _id = GUID 8f3ace1e-00be-4cd5-81a6-ff83ec3a4084;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "VelocityCorrection::VelocityCorrection";
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
					- m_transform = 0.286119 0 0 0.102496 26.4278 427.279 ;
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
							- _filename = "VelocityCorrection.sbs";
							- _subsystem = "VelocityCorrection";
							- _class = "VelocityCorrection";
							- _name = "vCorrectionTask(*void)";
							- _id = GUID 96aae243-9aad-45bf-b42c-d56ec46a399a;
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
						- _class = "VelocityCorrection";
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
					- m_transform = 0.472144 0 0 0.15508 716.056 368.979 ;
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
					- frameset = "<frameset rows=26%,74%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "adcAdcCurrentAdc";
							- _id = GUID 50da7754-1605-4098-b62f-9b22371009b9;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 4;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "adcAdcInstanciate(char,char,portId)";
							- _id = GUID 69b09e8e-859c-4432-b9f2-99c1e22469fb;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "vAdcGetValue(adc,*char,site_t)";
							- _id = GUID 52fb15d2-71ff-4667-bf6a-079185ec50e9;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "vAdcInit()";
							- _id = GUID 83ab65e6-3bea-4c1c-8cb0-156541d4ca49;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Adc.sbs";
							- _subsystem = "Adc";
							- _class = "ADC";
							- _name = "vAdcInterruption()";
							- _id = GUID 61a6ba00-2b90-44c0-bc02-5721e1c14327;
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
					- m_drawBehavior = 2056;
					- m_transform = 0.287063 0 0 0.0980392 510.427 604.745 ;
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
							- _filename = "Calibrate.sbs";
							- _subsystem = "Calibrate";
							- _class = "Calibrate";
							- _name = "vCalibrateTask(*void)";
							- _id = GUID 08352d71-e1a6-4cd6-88d9-f03d7ddafcfe;
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
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Pwm.sbs";
							- _subsystem = "Pwm";
							- _class = "PWM";
							- _name = "vPwmInit(pwmDevice)";
							- _id = GUID 4f51c010-ca30-4ae8-a1f4-ad386e73cc89;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Pwm.sbs";
							- _subsystem = "Pwm";
							- _class = "PWM";
							- _name = "vPwmSetDutyCycle(pwmDevice,uint)";
							- _id = GUID 68012f6f-0b85-4746-80eb-bb8300b54d8c;
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
				{ CGIInheritance 
					- _id = GUID 085f54c7-1da8-46d6-85ea-9f872f8e97a2;
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
						- _filename = "Motor.sbs";
						- _subsystem = "Motor";
						- _class = "Motor";
						- _name = "PWM";
						- _id = GUID da6699c1-2c3b-4caa-be76-1937dfb560ae;
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
					- m_pSource = GUID fd999fbb-bade-4a45-9c1c-ef6f57aca4bc;
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
					- m_SourcePort = 969 625 ;
					- m_TargetPort = 19 952 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 5f974b66-f87a-4799-a387-433633a08cd6;
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
						- _filename = "SelfTest.sbs";
						- _subsystem = "SelfTest";
						- _class = "";
						- _name = "SelfTest";
						- _id = GUID 1f2b8f16-76cd-4df3-b24a-2440a1d83722;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "SelfTest::SelfTest";
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
					- m_transform = 0.262512 0 0 0.123886 978.475 -5.75848 ;
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
							- _filename = "SelfTest.sbs";
							- _subsystem = "SelfTest";
							- _class = "SelfTest";
							- _name = "vSelfTest()";
							- _id = GUID 1945588b-55a8-44b9-87e4-d558fa026131;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 542c7d30-d517-4186-a811-f7e051dda075;
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
						- _filename = "SelfTest.sbs";
						- _subsystem = "SelfTest";
						- _class = "SelfTest";
						- _name = "PWM";
						- _id = GUID 907acfc9-cc90-4635-b576-97066c5005da;
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
					- m_pSource = GUID 5f974b66-f87a-4799-a387-433633a08cd6;
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
					- m_SourcePort = 985 716 ;
					- m_TargetPort = 912 726 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 08c7c7ed-ce2d-4a1d-b36e-2064a4d0e0fa;
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
						- _filename = "SelfTest.sbs";
						- _subsystem = "SelfTest";
						- _class = "SelfTest";
						- _name = "ADC";
						- _id = GUID 87903468-c3f1-4aef-be40-faa2203a37c7;
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
					- m_pSource = GUID 5f974b66-f87a-4799-a387-433633a08cd6;
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
					- m_SourcePort = 653 1443 ;
					- m_TargetPort = 921 587 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID a53c1084-1d9e-433c-a0d1-6cd45afd619d;
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Main.sbs";
						- _subsystem = "Main";
						- _class = "";
						- _name = "Main";
						- _id = GUID fff3c873-da27-426a-80e1-007c81521709;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "Main::Main";
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
					- m_transform = 0.155807 0 0 0.0944742 318.688 273.918 ;
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
							- _filename = "Main.sbs";
							- _subsystem = "Main";
							- _class = "Main";
							- _name = "main()";
							- _id = GUID 099af860-d138-40c3-91de-e7bb75704156;
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
						- _class = "Main";
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
					- _id = GUID 4e3244ed-bc75-4d9b-9896-7ec5e2729e2a;
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
						- _class = "Main";
						- _name = "Encoder";
						- _id = GUID 3b74753d-ae9d-4b68-b537-2228e2fe8c40;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Encoder";
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
					- m_pTarget = GUID 275d7a3e-c980-41d4-9600-cb91b36dda72;
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
					- m_SourcePort = 124 371 ;
					- m_TargetPort = 910 1114 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 1232a9b8-d99e-4989-baa2-3655daf833ad;
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
						- _class = "Main";
						- _name = "SensorBar";
						- _id = GUID 9aa26348-5ff6-4061-a436-8a3e9cea2cb7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "SensorBar";
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
					- m_pTarget = GUID 82b51846-4320-493f-a573-067eb5131bc4;
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
					- m_SourcePort = 772 625 ;
					- m_TargetPort = 265 1120 ;
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
						- _class = "Main";
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
						- _class = "Main";
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
					- _id = GUID 507999a1-029c-431b-a2aa-c664062ff3f1;
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
						- _class = "Main";
						- _name = "SelfTest";
						- _id = GUID c0a1e693-f816-4073-8bd5-e2e47f43140c;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "SelfTest";
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
					- m_pTarget = GUID 5f974b66-f87a-4799-a387-433633a08cd6;
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
					- m_SourcePort = 747 393 ;
					- m_TargetPort = 139 708 ;
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
						- _class = "Main";
						- _name = "VelocityCorrection";
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
				{ CGIInheritance 
					- _id = GUID 613786c1-a595-47ca-a309-cebc75fae168;
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
						- _class = "Main";
						- _name = "Motor";
						- _id = GUID adef27a8-08d2-49f2-96f6-06206621f7ba;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Motor";
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
					- m_pTarget = GUID fd999fbb-bade-4a45-9c1c-ef6f57aca4bc;
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
					- m_SourcePort = 849 1440 ;
					- m_TargetPort = 94 382 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 0df5e380-c6f8-474d-9219-4f915d833055;
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
						- _filename = "SensorBar.sbs";
						- _subsystem = "SensorBar";
						- _class = "SensorBar";
						- _name = "ADC";
						- _id = GUID 6816c636-dccb-4b7d-8af1-642ef5caa72a;
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
					- m_pSource = GUID 82b51846-4320-493f-a573-067eb5131bc4;
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
					- m_SourcePort = 631 1359 ;
					- m_TargetPort = 434 709 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 392d6bb8-902d-447d-a20b-e6a47fbb19be;
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
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "LED";
						- _id = GUID c1be4624-d3cc-411e-83b2-2b36dc9c7929;
					}
					- m_pParent = GUID 61811d80-ab8e-47f3-b559-0f38c7876de0;
					- m_name = { CGIText 
						- m_str = "LED";
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
					- m_transform = 0.213409 0 0 0.132799 404.573 -18.6907 ;
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
					- frameset = "<frameset rows=33%,67%>
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
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "LED";
							- _name = "vLedInit()";
							- _id = GUID 0132ade4-443b-41f7-9b53-eca9f67b4881;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Default.sbs";
							- _subsystem = "Default";
							- _class = "LED";
							- _name = "vLedSet(led,char)";
							- _id = GUID dc50ecc6-2ab9-4e2a-9b38-51bc09314ddf;
						}
					}
				}
				{ CGIInheritance 
					- _id = GUID 1a6159b3-395a-4193-918e-18918d0ed52c;
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
						- _filename = "SelfTest.sbs";
						- _subsystem = "SelfTest";
						- _class = "SelfTest";
						- _name = "LED";
						- _id = GUID 0d8a6338-97a5-4bd7-8fc1-fc5f77ad480a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LED";
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
					- m_pSource = GUID 5f974b66-f87a-4799-a387-433633a08cd6;
					- m_sourceType = 'F';
					- m_pTarget = GUID 392d6bb8-902d-447d-a20b-e6a47fbb19be;
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
					- m_SourcePort = 170 499 ;
					- m_TargetPort = 199 736 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 338fb4f3-27b5-4d03-8b94-b15d26f7c26f;
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
						- _class = "Main";
						- _name = "LED";
						- _id = GUID 1c76e69c-312b-4681-a509-85a36957f0dc;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "LED";
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
					- m_pTarget = GUID 392d6bb8-902d-447d-a20b-e6a47fbb19be;
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
					- m_SourcePort = 560 393 ;
					- m_TargetPort = 302 1187 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
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
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID c8db5a9c-23d1-4ddf-bb1b-e2195780afba;
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
			- _objectCreation = "5110902212920152026000851";
			- _umlDependencyID = "3329";
			- _lastModifiedTime = "8.21.2015::22:24:25";
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
				- elementList = 12;
				{ CGIClass 
					- _id = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID d281e7c6-9220-4127-9a6c-3c98a8958ff2;
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
					- m_transform = 0.174342 0 0 0.115662 82 77.1794 ;
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
					- m_transform = 0.175165 0 0 0.110338 309 76.2765 ;
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
					- _id = GUID 679a2c7d-d1e3-434f-8097-1bc6da9223c2;
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
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "SensorBar.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "SensorBar";
						- _id = GUID 71e10367-4efc-4e82-960e-9f02755cec47;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "SensorBar";
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
					- m_transform = 0.175986 0 0 0.122457 307 213.996 ;
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
					- m_transform = 0.176809 0 0 0.125109 82 213 ;
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
					- _id = GUID 163a2296-845f-41c2-a08d-98af071828c9;
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
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "SelfTest.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "SelfTest";
						- _id = GUID eab1f781-5284-4f96-8edd-7271be1637c3;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "SelfTest";
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
					- m_transform = 0.177632 0 0 0.117033 533 215.041 ;
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
					- m_transform = 0.179276 0 0 0.122502 80 374 ;
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
					- _id = GUID 466de2ea-d7bf-4603-9d3f-f90eadb8f94b;
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
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Encoder.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Encoder";
						- _id = GUID 68038364-716f-447b-98ff-da4c40d2d83e;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Encoder";
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
					- m_transform = 0.175164 0 0 0.123371 307 372 ;
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
					- _id = GUID 06376b21-95ff-49e0-a561-a69df1ee61df;
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
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Motor.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Motor";
						- _id = GUID ff7b1e3e-7cc3-4f55-9636-78da1b858107;
					}
					- m_pParent = GUID e0b4d4cc-4ffe-4ea8-8bbb-81a51b545fca;
					- m_name = { CGIText 
						- m_str = "Motor";
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
					- m_transform = 0.179277 0 0 0.125109 80 532 ;
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
					- m_transform = 0.174342 0 0 0.126846 533 371.951 ;
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
				{ CGIPackage 
					- _id = GUID d27a0eae-cdcd-41ff-8b43-36ee6845beac;
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
					- m_transform = 0.174342 0 0 0.113814 534 75.2765 ;
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
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID c8db5a9c-23d1-4ddf-bb1b-e2195780afba;
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

